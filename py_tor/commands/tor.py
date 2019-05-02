import os
import requests 
import py_tor.utility as utility

START_TOR_MESSAGE = r"""

      ___                         ___           ___                                                ___           ___     
     /  /\          ___          /  /\         /  /\          ___                    ___          /  /\         /  /\    
    /  /::\        /__/\        /  /::\       /  /::\        /__/\                  /__/\        /  /::\       /  /::\   
   /__/:/\:\       \  \:\      /  /:/\:\     /  /:/\:\       \  \:\                 \  \:\      /  /:/\:\     /  /:/\:\  
  _\_ \:\ \:\       \__\:\    /  /::\ \:\   /  /::\ \:\       \__\:\                 \__\:\    /  /:/  \:\   /  /::\ \:\ 
 /__/\ \:\ \:\      /  /::\  /__/:/\:\_\:\ /__/:/\:\_\:\      /  /::\                /  /::\  /__/:/ \__\:\ /__/:/\:\_\:\
 \  \:\ \:\_\/     /  /:/\:\ \__\/  \:\/:/ \__\/~|::\/:/     /  /:/\:\              /  /:/\:\ \  \:\ /  /:/ \__\/~|::\/:/
  \  \:\_\:\      /  /:/__\/      \__\::/     |  |:|::/     /  /:/__\/             /  /:/__\/  \  \:\  /:/     |  |:|::/ 
   \  \:\/:/     /__/:/           /  /:/      |  |:|\/     /__/:/                 /__/:/        \  \:\/:/      |  |:|\/  
    \  \::/      \__\/           /__/:/       |__|:|~      \__\/                  \__\/          \  \::/       |__|:|~   
     \__\/                       \__\/         \__\|                                              \__\/         \__\|  


                """

def run(arg, interface):
    try:
        rootDir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        if arg == "start":
            command = rootDir + "/scripts/internal/start_tor " + interface   
            background = True  
            message = START_TOR_MESSAGE       
        else:
            command = rootDir + "/scripts/internal/stop_tor " + interface
            background = False
            message = ""
        
        utility.subprocess_cmd(command, background, message)
            
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
        print("NO....")