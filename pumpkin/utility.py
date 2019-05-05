import subprocess
import sys
import time

def subprocess_cmd(commands, background, message):
    print("Background: ", background)
    if background == False:
        process = subprocess.Popen(commands, stdout=subprocess.PIPE, shell=True)
        proc_stdout = process.communicate()[0].strip()

        out_str = proc_stdout.decode(sys.stdout.encoding)
        timed_log(out_str.split('\n'))
    else:
        print(message)
        process = subprocess.Popen("sudo "+ commands +" > tor_start.log", stdout=subprocess.PIPE, shell=True)
        out_str = proc_stdout = process.communicate()
    
    return out_str

def timed_log(lines):
    for line in lines:
        print(line)

def index_of(element, array):
    try:
        return array.index(element)
    except:
        return -1