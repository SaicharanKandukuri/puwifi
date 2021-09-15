import copy,sys,urllib,loginpu

from requests.models import Response
from signal import signal, SIGINT
from sys import exit
from time import sleep
import urllib.request as urllib2

"""
Accept user input and pass it to the loginpu module
    script <username> <password>
        url is set to deafault value http://10.0.0.11:8090/login.xml        
"""
x=0
def basic_login_nosys(username, password):
    """
    Accept user input and pass it to the loginpu module
        main.py <username> <password>
            url is set to deafault value http://10.0.0.11:8090/login.xml        
    """
    url = "http://10.0.0.11:8090/login.xml"

    response = copy.deepcopy(loginpu.login(url, username, password))
    return [response]

def keep_alive(username=sys.argv[1], password=sys.argv[2],interval=2): # 5 is suggested
    """
    Runs script forever to keep wifi connected logged in
    """
    try:
        req = urllib2.Request("http://10.0.0.11:8090/", headers={'User-Agent':'Mozilla/5.0'})
        urllib2.urlopen(req)
        print("Check: \"Parul_WIFI\" connected")
    except urllib.error.URLError:
        print("Could not see \"PARUL_WIFI\"")
        print("Try Connecting to wifi")
        print(x+1)
    try:
        req2 = urllib2.Request("https://www.google.com", headers={'User-Agent':'Mozilla/5.0'}); urllib2.urlopen(req2)
        print("Internet Connection Avalible")
    except urllib.error.URLError:
        print("Attempting To Sign In " + username )
        response = copy.deepcopy(basic_login_nosys(username, password))
        print("looged in as " + username)
        # print("------\nStatus: " + response[3]+ "\n------")        
    sleep(interval)
        

def handler(signal_received, frame):
    # Handle any cleanup here
    print('\nSIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

if __name__ == '__main__':
    # Tell Python to run the handler() function when SIGINT is recieved
    signal(SIGINT, handler)

    print('Running '+sys.argv[0]+'. Press CTRL-C to exit.')
    while True:
        keep_alive(sys.argv[1], sys.argv[2])
