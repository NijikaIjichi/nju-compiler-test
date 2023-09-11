import json
from os import system
from itertools import count, zip_longest

def msg(s):
    print('\033[1m\033[91m' + s + '\033[0m\033[0m');
def err(data_in, s):
    msg("Wrong on input " + str(data_in) + "\n" + s)
    exit(1)

spim_file = "./workdir/a.s"
f_json    = "./workdir/a.json"
program   = "spim -lstack 1048576 -stext 1048576 -file"
spim_in   = './workdir/spim_in'
spim_out  = './workdir/spim_out'
flags = ''

def only_nums(g):
    for s in g:
        try:
            i = int(s)
            yield i
        except ValueError:
            pass

for data_in, data_out, ret_val in json.load(open(f_json)):
    with open(spim_in, 'w') as to_spim_w:
        for i in data_in:
            to_spim_w.write(str(i) + '\n')

    ret = system(f"{program} {flags} {spim_file} < {spim_in} 2>/dev/null | sed -e s/'\(Enter an integer:\)\+'/''/ > {spim_out}")
    if ret != 0:
        with open(spim_out, 'r') as from_spim_r:
            err(data_in,
                "runtime error occured when running your IR code\n")
    with open(spim_out, 'r') as from_spim_r:
        for idx, (expect, user_out) in enumerate(zip_longest(data_out, only_nums(from_spim_r))):
            if expect == None:
                err(data_in, "Output mismatch!(you output more than supposed)")
            if user_out == None:
                err(data_in, "Output mismatch!(you output less than supposed)")
            if expect != user_out:
                err(data_in, "Output mismatch! expected %d, found %d at line %d" % (expect, user_out, idx))
        else:
            pass

exit(0)
