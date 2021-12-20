import optparse
from sys import getsizeof
import logging
import requests
import time

from rich.logging import RichHandler
from signal import signal, SIGINT

FORMAT = "%(message)s"

logging.basicConfig(
    level="NOTSET",
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler()]
)

logging.disable('DEBUG')

log = logging.getLogger("rich")


class wifi_utils:

    def __init__(self, username, password, host, port):
        self.username = username
        self.password = password
        self.host = host
        self.port = port

    def request(self,
                method,
                username,
                password,
                host, port,
                timeout) -> list:
        # print(type(host))
        # print(type(port))
        # print(type(method))
        # print(host)
        # print(method)
        # print(port)
        url = ("http://"+host+":"+port+"/"+method)
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
              method="login.xml",
              timeout=10) -> list:
        return self.request(method, username, password, host, port, timeout)

    def logout(self,
               username,
               password,
               host,
               port,
               method="logout.xml",
               timeout=10) -> list:
        return self.request(method, username, password, host, port, timeout)

# def get_xml_msg(xml): # for later (●'◡'●)
#     return Et.parse(xml).getroot()[1]

def connection_to(url, timeout=10):
    try:
        requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError,
            requests.Timeout):
        return False


def keep_alive(username, password, host, port):
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
                log.info(wifi_utils.login(username, password, host, port))
            except (requests.ConnectionError,
                    requests.Timeout):
                log.critical(
                    "Connection error: \"UNSTABLE CONNECTION TO HOST\"")

        time.sleep(5)


def exit_handler(signal_received, frame):
    log.warning('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)


if __name__ == '__main__':

    signal(SIGINT, exit_handler)

    parser = optparse.OptionParser()
    parser.add_option('-u', '--username', dest='username',
                      help='username to login/logout with parul university wifi service')
    parser.add_option('-p', '--password', dest='password',
                      help='password to login/logout with parul university wifi service')
    parser.add_option('-H', '--host', dest='host',
                      default='10.0.0.11', type=str)
    parser.add_option('-P', '--port', dest='port',
                      default='8090', type=str)
    parser.add_option('-k', '--keep-alive', action='store_true',
                      help='keep connecting to wifi when it gets signed out', default=False)
    parser.add_option('-o', '--logout', action='store_true',
                      help='logout from wifi', default=False)
    parser.add_option('-l', '--login', action='store_true',
                      help='login to wifi', default=False)

    options, args = parser.parse_args()

    wifi_utils = wifi_utils(
        options.username, options.password, options.host, options.port)

    if options.login:
        log.info("=> login <=")
        log.info(wifi_utils.login(options.username,
                         options.password,
                         options.host, options.port,
                        ))
        exit(0)

    if options.logout:
        log.info("=> logout <=")
        log.info(wifi_utils.logout(options.username,
                          options.password,
                          options.host, options.port,
                          ))
        exit(0)

    if options.keep_alive:
        log.info("=> keep alive <=")
        keep_alive(options.username,
                   options.password,
                   options.host, options.port,
                   )
