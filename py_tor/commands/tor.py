import os
import requests 
import py_tor.utility as utility

def run(arg, interface):
    try:
        rootDir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        if arg == "start":
            command = rootDir + "/scripts/internal/start_tor " + interface            
        else:
            command = rootDir + "/scripts/internal/stop_tor " + interface

        utility.subprocess_cmd(command)
    except Exception as e:
        raise e