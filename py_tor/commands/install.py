import os
import py_tor.utility as utility

def install_all():
    try:
        rootDir = os.path.abspath(os.curdir)
        command = rootDir + "/scripts/internal/install"
        utility.subprocess_cmd(command)
    except Exception as e:
        raise e