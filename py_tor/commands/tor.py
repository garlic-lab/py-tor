import os
import requests 
import py_tor.utility as utility

def run(arg, interface):
    try:
        background = False
        message = ""
        rootDir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
            statusResponse = utility.subprocess_cmd(command, background, message)
            status()
            
    except Exception as e:
        raise e

def status():
    try:
        print("STATUS:")

        # Local config


        # Public IP
        session = requests.session()
        session.proxies = {}
        session.proxies['http'] = 'socks5h://localhost:9050'
        session.proxies['https'] = 'socks5h://localhost:9050'

        oldIp = requests.get('https://api.ipify.org/?format=json')
        newIp = session.get('https://api.ipify.org/?format=json')

        print("Your IP without Tor: " + oldIp.text)
        print("Your IP with Tor " + newIp.text)
    except Exception as e:
        print(e)