# test/check.py
import json
import sys
import subprocess
from itertools import count

def err(data_in, s):
    print(f'\033[1m\033[91mWrong on input {data_in}\n{s}\033[0m', file=sys.stderr)
    sys.exit(1)

if len(sys.argv) != 3:
    print("Usage: python3 check.py <ir_file> <json_file>")
    sys.exit(1)

f_ir = sys.argv[1]
f_json = sys.argv[2]
program = "irsim/build/irsim"
total_instructions = 0

with open(f_json) as f:
    test_cases = json.load(f)

for data_in, data_out, ret_val in test_cases:
    # 在内存中构建输入，避免写文件产生的竞态条件
    input_str = '\n'.join(map(str, data_in)) + '\n'
    
    proc = subprocess.run(
        [program, f_ir],
        input=input_str,
        text=True,
        capture_output=True
    )
    
    if proc.returncode != 0:
        err(data_in, f"runtime error occured when running your IR code\n{proc.stderr.strip() or proc.stdout.strip()}")

    out_lines = [line.strip() for line in proc.stdout.strip().splitlines()]
    
    try:
        for idx, expect in zip(count(1), data_out):
            if idx - 1 >= len(out_lines):
                err(data_in, "Output mismatch!(you output less than supposed?)")
            user_out = int(out_lines[idx - 1])
            if expect != user_out:
                err(data_in, f"Output mismatch! expected {expect}, found {user_out} at line {idx}")
        
        if len(out_lines) <= len(data_out):
            err(data_in, "Output mismatch!(you output less than supposed?)")
            
        s = out_lines[len(data_out)]
        if not s.startswith("return"):
            err(data_in, "Output mismatch!(you output more than supposed?)")
            
        single = int(s.split()[3])
        total_instructions += single
        
    except ValueError:
        err(data_in, "Output mismatch!(formatting error)")

# 仅输出指令数供主进程采集
print(total_instructions)
sys.exit(0)