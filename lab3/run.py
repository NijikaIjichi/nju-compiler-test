# test/run.py
import argparse
import subprocess
import sys
import os
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

RED, GREEN, NC = '\033[0;31m', '\033[0;32m', '\033[0m'
BOLD, NORMAL = '\033[1m', '\033[0m'

def parse_args():
    parser = argparse.ArgumentParser(description="Compiler Parallel Test Runner")
    parser.add_argument("-r", "--run", required=True, help="parser executable path")
    parser.add_argument("-e", "--extend", choices=['base', 'extend1', 'extend2', 'both', 'prf'], default='base')
    parser.add_argument("-a", "--advance", action='store_true', help="test advance")
    parser.add_argument("-c", "--continue_on_error", action='store_true', help="do not stop when test failed")
    parser.add_argument("-t", "--timeout", type=int, default=10, help="timeout per test")
    parser.add_argument("-j", "--jobs", type=int, default=os.cpu_count(), help="parallel jobs")
    return parser.parse_args()

args = parse_args()

print("Making(Updating) irsim...")
subprocess.run(["make", "-C", "irsim"], check=True)
Path("workdir").mkdir(exist_ok=True)

# 自动递归搜索对应大类下的所有测试
def get_tests(category):
    return list(Path("tests").rglob(f"{category}/**/*.cmm"))

tests_dict = {
    'base': get_tests('base'),
    'advance': get_tests('advance'),
    'extend1': get_tests('extend/1'),
    'extend2': get_tests('extend/2'),
    'both': get_tests('extend/both'),
    'prf': get_tests('extend/prf')
}

should_pass = tests_dict['base'].copy()
if args.advance:
    should_pass.extend(tests_dict['advance'])

should_fail = []
if args.extend == 'extend1':
    should_pass.extend(tests_dict['extend1'])
    should_fail.extend(tests_dict['extend2'] + tests_dict['both'] + tests_dict['prf'])
elif args.extend == 'extend2':
    should_pass.extend(tests_dict['extend2'])
    should_fail.extend(tests_dict['extend1'] + tests_dict['both'] + tests_dict['prf'])
elif args.extend == 'both':
    should_pass.extend(tests_dict['extend1'] + tests_dict['extend2'] + tests_dict['both'])
elif args.extend == 'prf':
    should_pass.extend(tests_dict['extend1'] + tests_dict['extend2'] + tests_dict['both'] + tests_dict['prf'])

total_passed = 0
total_instructions = 0
lock = threading.Lock()

def run_single_test(cmm_file, expect_pass):
    global total_passed, total_instructions
    
    # 构造唯一的中间文件名: tests/base/2018/test1.cmm -> base_2018_test1.ir
    rel_name = str(cmm_file.relative_to("tests")).replace(os.sep, '_').replace('.cmm', '.ir')
    ir_file = Path("workdir") / rel_name
    json_file = cmm_file.with_suffix('.json')
    
    if ir_file.exists():
        ir_file.unlink()
        
    try:
        subprocess.run([args.run, str(cmm_file), str(ir_file)], 
                       timeout=args.timeout, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except subprocess.TimeoutExpired:
        return False, "TLE", 0

    if expect_pass:
        if not ir_file.exists():
            return False, "Should translate but failed", 0
            
        chk = subprocess.run(["python3", "check.py", str(ir_file), str(json_file)], 
                             timeout=args.timeout, capture_output=True, text=True)
        if chk.returncode == 0:
            inst = int(chk.stdout.strip())
            return True, f"matched ({inst} inst)", inst
        else:
            return False, f"mismatch: {chk.stderr.strip()}", 0
    else:
        if ir_file.exists():
            return False, "Should not translate", 0
        return True, "passed (fault test)", 0

with ThreadPoolExecutor(max_workers=args.jobs) as executor:
    futures = {executor.submit(run_single_test, t, True): t for t in should_pass}
    futures.update({executor.submit(run_single_test, t, False): t for t in should_fail})
    
    for future in as_completed(futures):
        t = futures[future]
        try:
            passed, msg, inst = future.result()
        except Exception as e:
            passed, msg, inst = False, str(e), 0
            
        with lock:
            # 获取相对于 tests 目录的路径，例如：base/2018/test1.cmm
            rel_path = t.relative_to("tests") 
            
            if passed:
                total_passed += 1
                total_instructions += inst
                print(f"test [{rel_path}] {msg}")
            else:
                print(f"{RED}{BOLD}test [{rel_path}] {msg}{NC}{NORMAL}")
                if not args.continue_on_error:
                    print(f"{RED}Exiting due to error. Run with -c to continue on error.{NC}")
                    os._exit(1)

print(f"\nPASSED {total_passed}/{len(should_pass) + len(should_fail)}")
if total_instructions > 0:
    print(f"irsim executes about {total_instructions} instructions")