import os
import sys
import requests 
import pumpkin.utility as utility

def run(arg, interface, background):
    try:
        torIsRunning = False 
        message      = ""
        rootDir      = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        if arg == "start":
            command = "bash " + rootDir + "/scripts/tor/setup " + interface   
            utility.subprocess_cmd(command, background, 'Setup local configurations')     
            if sys.platform == "darwin": 
                utility.subprocess_cmd('tor', background, 'Startup Tor process')

            if sys.platform == "linux": 
                utility.subprocess_cmd('sudo service tor start', background, 'Startup Tor process')
                utility.subprocess_cmd('sudo service privoxy start', background, 'Startup Tor process')
        
        if arg == "stop":
            command = "bash " + rootDir + "/scripts/tor/stop " + interface
            utility.subprocess_cmd(command, False, message)

        if arg == "status":
            command = "bash " + rootDir + "/scripts/tor/status " + interface
            subprocessResp = utility.subprocess_cmd(command, False, message)

            if sys.platform == "darwin":
                subprocessResp = subprocessResp.split(" ")
                if utility.index_of('Yes', subprocessResp) >= 0:
                    torIsRunning = True 
            
            if sys.platform == "linux":
                subprocessResp = subprocessResp.split(" ")
                if utility.index_of('active', subprocessResp) >= 0:
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
            print("Tor is down")
            print("Your public IP: " + ipWithoutTor.text)

    except Exception as e:
        print(e)
