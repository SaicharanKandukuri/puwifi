import optparse
from sys import getsizeof
import xml.etree.ElementTree as ET
import logging
import requests

from rich.logging import RichHandler
from signal import signal, SIGINT

FORMAT = "%(message)s"

logging.basicConfig(
    level="NOTSET", 
    format=FORMAT, 
    datefmt="[%X]", 
    handlers=[RichHandler()]
)

log = logging.getLogger("rich")


class wifi_utils:

    def __init__(self, username, password, host, port):
        self.username = username
        self.password = password
        self.host = host
        self.port = port

    def request(self,
                type,
                username,
                password,
                host, port,
                timeout=10) -> list:

        url = ("http://"+host+":"+port+"/"+type)
        body = ("mode=191&username=" + username + "&password=" + password +
                "&a=1630404423764&producttype=0"
                )
        headers = {
            "Host": "http://"+host+"/"+port+"",
            "Content-Length": getsizeof(body),
            "User-Agent": "Chrome/92.0.4515.159 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Origin": "http://"+host+"/"+port,
            "Referer": "http://"+host+"/"+port+"/",
            "Accept-Encoding": "gzip defalte",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "close",
        }
        body_array = bytearray(body, 'utf-8')

        r = requests.post(url,
                          data=body_array,
                          headers=headers,
                          timeout=timeout,
                          verify=False
                          )
        return [(r.status_code == 200), r.text, r.status_code]

    def login(self,
              username,
              password,
              host,
              port,
              type="login.xml",
              timeout=10) -> list:
        
        return self.request("login.xml", username, password, host, port)

    def logout(self,
               username,
               password,
               host,
               port,
               type="logout.xml",
               timeout=10) -> list:
        return self.request("logout.xml",username, password, host, port)

def connection_to(url, timeout=10):
    try:
        requests.get(url, timeout=timeout)
        return 0
    except (requests.ConnectionError, 
            requests.Timeout):
        return 1

def keep_alive(username, password,host,port):
    while True:
        
        if connection_to("http://10.0.0.11:8090/"):
            log.info("connection to router \"avalible\"")
        else:
            log.error("connection to router \"unavalible\"")
        
        if connection_to("https://google.com") == 0:
            log.info("Connected to the internet")
        else:
            log.error("Not connected to the internet")
            log.info("Tying to reconnect with "+ 
                     username + " password: " + password)
            log.info(wifi_utils.keep_alive(username, password,host,port))

def exit_handler(signal_received, frame):
    log.warning('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)


if __name__ == '__main__':
    
    signal(SIGINT, exit_handler)
    
    parser = optparse.OptionParser()
    parser.add_option('m', '--mode', dest='mode', type='string',
                      help='mode of operation login/logut', default='login')
    parser.add_option('-u', '--username', dest='username',
                      help='username to login/logut with parul university wifi service')
    parser.add_option('-p', '--password', dest='password',
                      help='password to login/logout with parul university wifi service')
    parser.add_option('-H', '--host', dest='host',
                      default='10.0.0.11')
    parser.add_option('-P', '--port', dest='port',
                      default='8090')
    parser.add_option('-k', '--keep-alive', action='store_true',
                       help='keep connecting to wifi when it gets signed out', default=False)
    parser.add_option('-lo', '--logout', action='store_true', help='logout from wifi', default=False)
    parser.add_option('-l', '--login', action='store_true', help='login to wifi', default=False)
    
    options, args = parser.parse_args()

    keep_alive(options.username, options.password, options.host, options.port)
    
