import os
import py_tor.utility as utility

def run(arg, interface):
    try:
        rootDir = os.path.abspath(os.curdir)
        if arg == "start":
            command = rootDir + "/scripts/internal/start_tor " + interface            
        else:
            command = rootDir + "/scripts/internal/stop_tor " + interface

        utility.subprocess_cmd(command)
    except Exception as e:
        raise e