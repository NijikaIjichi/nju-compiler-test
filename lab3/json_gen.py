import json
from os.path import splitext
from sys import argv
from os import system

def msg(s):
    print('\033[1m\033[91m' + s + '\033[0m\033[0m');
def err(data_in, s):
    msg("Wrong on input " + str(data_in) + "\n" + s)
    exit(1)

if len(argv) != 3:
    print("Usage: python json_gen.py [IR file] [json file]")
    print("Usage: python json_gen.py [cmm file] [json file]")
    print("This program will read from given json file, ignore the output")
    print("And using your output this time to overwrite the original output in json file")
    print("So, you can leave the output in json as [], and just give the input to automatically generate a json file")
    msg("Do not run more than one instance of this program or check.py parallelly!")
    exit(0)

if splitext(argv[1])[1] == ".cmm":
    f_ir = "workdir/a.ir"
    print("Given a cmm file")
    cmd = "./parser %s %s"%(argv[1], f_ir)
    print("Running command: " + cmd + " to generate IR")
    system(cmd)
elif splitext(argv[1])[1] == ".ir":
    f_ir = argv[1]
else:
    msg(argv[1] + "is neither a cmm file nor an IR file!")
    exit(1)

if splitext(argv[2])[1] != ".json":
    msg(argv[2] + " is not an valid json file!")
    exit(1)

f_json = argv[2]
program = "irsim/build/irsim"
irsim_in  = './workdir/irsim_in'
irsim_out = './workdir/irsim_out'

data_with_output = []

for data_in, dummy, ret_val in json.load(open(f_json)):
    with open(irsim_in, 'w') as to_irsim_w:
        for i in data_in:
            to_irsim_w.write(str(i) + '\n')

    ret = system("%s %s < %s > %s 2>/dev/null"%(program, f_ir , irsim_in , irsim_out))
    # Suppose irsim is compiled by run.sh
    if ret != 0:
        with open(irsim_out, 'r') as from_irsim_r:
            err(data_in,
                "runtime error occured when running your IR code\n"
                + from_irsim_r.read().splitlines()[-1]);
    with open(irsim_out, 'r') as from_irsim_r:
        output_lines = from_irsim_r.readlines()[:-1]
        output_lines = list(map(int, output_lines))
        data_with_output.append([data_in, output_lines, 0])

with open(f_json, "w") as out:
    json.dump(data_with_output, out)

print("json file updated successfully")
