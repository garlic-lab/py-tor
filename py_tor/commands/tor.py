import os
import sys
import requests 
import py_tor.utility as utility

def run(arg, interface):
    try:
        background   = False
        torIsRunning = False 
        message      = ""
        rootDir      = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        if arg == "start":
            command = "sudo bash " + rootDir + "/scripts/internal/setup_tor " + interface   
            utility.subprocess_cmd(command, False, 'Setup local configurations')      
            utility.subprocess_cmd('tor', True, 'Startup Tor process')
        
        if arg == "stop":
            command = "bash " + rootDir + "/scripts/internal/stop_tor " + interface
            utility.subprocess_cmd(command, background, message)

        if arg == "status":
            command = "bash " + rootDir + "/scripts/internal/status_tor " + interface
            subprocessResp = utility.subprocess_cmd(command, background, message)

            # parse subprocess response by OS
            if sys.platform == "darwin":
                subprocessResp = subprocessResp.split(" ")
                if utility.index_of('Yes', subprocessResp) >= 0:
                    torIsRunning = True 

            status(torIsRunning)
            
    except Exception as e:
        raise e

def status(torIsRunning):
    try:
        ipifyHost  = 'https://api.ipify.org'
        localSocks = 'socks5h://localhost:9050'
        ipWithoutTor = requests.get(ipifyHost)

        if torIsRunning:
            print("Tor is running 👻")

            session = requests.session()
            session.proxies = {}
            session.proxies['http']  = localSocks
            session.proxies['https'] = localSocks

            ipWithTor = session.get(ipifyHost)

            print("Your public IP without Tor: " + ipWithoutTor.text)
            print("Your public IP with Tor: "    + ipWithTor.text)
        else:
            print("Tor is down 💩")
            print("Your public IP: " + ipWithoutTor.text)

    except Exception as e:
        print(e)