import subprocess
import sys
import time

def subprocess_cmd(commands, background, message):
    if background == False:
        process = subprocess.Popen(commands, stdout=subprocess.PIPE, shell=True)
        proc_stdout = process.communicate()[0].strip()

        out_str = proc_stdout.decode(sys.stdout.encoding)
        timed_log(out_str.split('\n'))
    else:
        print(message)
        process = subprocess.Popen("nohup "+ commands +" &", shell=True)
        out_str = proc_stdout = process.communicate()
    
    return out_str

def timed_log(lines):
    for line in lines:
        print(line)
        time.sleep(1)

def index_of(element, array):
    try:
        return array.index(element)
    except:
        return -1