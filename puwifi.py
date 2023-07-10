import argparse
import sys
from sys import getsizeof
import logging
from signal import signal, SIGINT
import time
import requests

# MIT License
#
# Copyright (c) 2022 SaicharanKandukuri
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from rich.logging import RichHandler


FORMAT = "%(message)s"

logging.basicConfig(
    level="NOTSET",
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler()]
)

logging.disable('DEBUG')

log = logging.getLogger("rich")


class WifiUtils:
    """class for wifi utils"""
    def __init__(self, username, password, host, port):
        self.username = username
        self.password = password
        self.host = host
        self.port = port

    @classmethod
    def request(cls,
                method,
                username,
                password,
                host, port,
                timeout) -> list:
        """request method: sends request to wifi host

        Args:
            method (str): interaction method "login.xml" or "logout.xml". Defaults to "login.xml".
            username (str): username assigned by parul university to access wifi
            password (str): password assigned by parul university to access wifi
            host (str): hostname of the parul university wifi hotspot/routers Defaults to "
            port (str): port to send login request. Defaults to "8090".
            timeout (int): request timeout. Defaults to 10.

        Returns:
            list
            server_request status[true|false]
            response(xml data returned form server)
            status_code(web request status code)
        """
        url = "http://"+host+":"+port+"/"+method
        body = ("mode=191&username=" + username + "&password=" + password +
                "&a=1630404423764&producttype=0"
                )
        headers = {
            "Host": "http://" + host + ":" + port + "",
            "Content-Length": str(getsizeof(body)),
            "User-Agent": "Chrome/92.0.4515.159 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Origin": "http://" + host + ":" + port,
            "Referer": "http://" + host + ":" + port + "/",
            "Accept-Encoding": "gzip defalte",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "close",
        }
        body_array = bytearray(body, 'utf-8')

        req = requests.post(url,
                          data=body_array,
                          headers=headers,
                          timeout=timeout,
                          verify=False
                          )
        return [(req.status_code == 200), req.text, req.status_code]

    def login(self,
              username,
              password,
              host,
              port="8090",
              method="login.xml",
              timeout=10) -> list:
        """login: uses request method to send login web request with credentials to wifi host

        Args:
            username (str): username assigned by parul university to access wifi
            password (str): password assigned by parul university to access wifi
            host (str): hostname of the parul university wifi hotspot/routers
            Defaults to "10.0.0.11"
            port (str, optional): port to send login request. Defaults to "8090".
            method (str, optional): interaction method
            "login.xml" or "logout.xml". Defaults to "login.xml".
            timeout (int, optional): request timeout. Defaults to 10.
        """
        return self.request(method, username, password, host, port, timeout)

    def logout(self,
               username,
               password,
               host,
               port="8090",
               method="logout.xml",
               timeout=10) -> list:
        """logout: uses request method to send logout web request with credentials to wifi host

        Args:
            username (str): username assigned by parul university to access wifi
            password (str): password assigned by parul university to access wifi
            host (str): hostname of the parul university wifi hotspot/routers
            Defaults to "10.0.0.11"
            port (str, optional): port to send login request. Defaults to "8090".
            method (str, optional): interaction method
            "login.xml" or "logout.xml". Defaults to "logout.xml".
            timeout (int, optional): request timeout. Defaults to 10.
        """
        return self.request(method, username, password, host, port, timeout)

# def get_xml_msg(xml): # for later (●'◡'●)
#     return Et.parse(xml).getroot()[1]

def grey_print(_string):
    """prints outs grey text

    Args:
        _string (str)
    """
    print(f"\033[90m{_string}\033[0m")
def connection_to(url, timeout=10):
    """checks if connection to url is available"""
    try:
        requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError,
            requests.Timeout):
        return False


def keep_alive(username, password, host, port):
    """keeps connection alive to wifi host"""
    while True:

        if connection_to("http://10.0.0.11:8090/"):
            log.info("connection to router \"available\"")
        else:
            log.critical("connection to router \"unavailable\"")

        if connection_to("https://google.com"):
            log.info("Connected to the internet")
        else:
            log.warning("Not connected to the internet")
            log.info("Tying to login back")
            try:
                log.info(WifiUtils.login(username, password, host, port))
            except (requests.ConnectionError,
                    requests.Timeout):
                log.critical(
                    "Connection error: \"UNSTABLE CONNECTION TO HOST\"")

        time.sleep(5)

def exit_handler(_signal, frame):
    """captures keyboard interrupts and kill signals & exits with messesage"""
    log.warning('SIGINT or CTRL-C detected. Exiting gracefully')
    grey_print("signal:"+str(_signal))
    grey_print("frame:"+str(frame))
    sys.exit(0)


def main():
    """Entry point
    """
    signal(SIGINT, exit_handler)

    parser = argparse.ArgumentParser(
        prog='puwifi', 
        description='parul university wifi login/logout tool',
        epilog="🍵 made by @SaicharanKandukuri"
        )
    
    parser.add_argument('-u', '--username', dest='username',
                      help='username to login/logout with parul university wifi service')
    parser.add_argument('-p', '--password', dest='password',
                      help='password to login/logout with parul university wifi service')
    parser.add_argument('-H', '--host', dest='host',
                      default='10.0.0.11', type=str)
    parser.add_argument('-P', '--port', dest='port',
                      default='8090', type=str)
    parser.add_argument('-k', '--keep-alive', action='store_true',
                      help='keep connecting to wifi when it gets signed out', default=False)
    parser.add_argument('-o', '--logout', action='store_true',
                      help='logout from wifi', default=False)
    parser.add_argument('-l', '--login', action='store_true',
                      help='login to wifi', default=False)
    
    args = parser.parse_args()
    
    if not sys.argv[1:]:
        print("no arguments passed")
        print(parser.print_help())
    
    if args.login:
        log.info("=> login <=")
        log.info(WifiUtils.login(args.username,
                         args.password,
                         args.host, args.port,
                        ))
        sys.exit(0)
    
    if args.logout:
        log.info("=> logout <=")
        log.info(WifiUtils.logout(args.username,
                          args.password,
                          args.host, args.port,
                          ))
        sys.exit(0)
    
    if args.keep_alive:
        log.info("=> keep alive <=")
        keep_alive(args.username,
                   args.password,
                   args.host, args.port,
                   )
    
