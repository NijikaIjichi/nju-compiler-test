# test/json_gen.py
import json
import sys
import subprocess
from os.path import splitext
from pathlib import Path

def err(data_in, s):
    print(f'\033[1m\033[91mWrong on input {data_in}\n{s}\033[0m', file=sys.stderr)
    sys.exit(1)

if len(sys.argv) != 3:
    print("Usage: python3 json_gen.py [IR file | cmm file] [json file]")
    sys.exit(0)

f_in = sys.argv[1]
f_json = sys.argv[2]
program = "./irsim/build/irsim"

if splitext(f_in)[1] == ".cmm":
    Path("workdir").mkdir(exist_ok=True)
    f_ir = f"workdir/temp_{Path(f_in).stem}.ir"
    print(f"Given a cmm file, running parser to generate IR...")
    subprocess.run(["./parser", f_in, f_ir], check=True)
elif splitext(f_in)[1] == ".ir":
    f_ir = f_in
else:
    print("Invalid file type")
    sys.exit(1)

data_with_output = []
with open(f_json) as f:
    test_cases = json.load(f)

for data_in, dummy, ret_val in test_cases:
    input_str = '\n'.join(map(str, data_in)) + '\n'
    proc = subprocess.run([program, f_ir], input=input_str, text=True, capture_output=True)
    
    if proc.returncode != 0:
         err(data_in, f"Runtime error:\n{proc.stderr}")
         
    # 获取除最后一行（return X ...）外的所有输出行
    out_lines = [int(x) for x in proc.stdout.strip().splitlines()[:-1]]
    data_with_output.append([data_in, out_lines, 0])

with open(f_json, "w") as out:
    json.dump(data_with_output, out, indent=4)

print("json file updated successfully")