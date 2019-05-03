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
            command = "bash " + rootDir + "/scripts/internal/start_tor " + interface   
            background = True  
            message = "Startup Tor" 
            utility.subprocess_cmd(command, background, message)      
        
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
        ipWithoutTor = requests.get('https://api.ipify.org/?format=json')

        if torIsRunning:
            print("Tor is running 👻")

            session = requests.session()
            session.proxies = {}
            session.proxies['http'] = 'socks5h://localhost:9050'
            session.proxies['https'] = 'socks5h://localhost:9050'

            ipWithTor = session.get('https://api.ipify.org/?format=json')

            print("Your public IP without Tor: " + ipWithoutTor.text)
            print("Your public IP with Tor: " + ipWithTor.text)
        else:
            print("Tor is down 💩")
            print("Your public IP: " + ipWithoutTor.text)

    except Exception as e:
        print(e)