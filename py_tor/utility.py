import subprocess
import sys
import time

def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()

    out_str = proc_stdout.decode(sys.stdout.encoding)
    timed_log(out_str.split('\n'))
    return proc_stdout

def timed_log(lines):
    for line in lines:
        print(line)
        time.sleep(1)