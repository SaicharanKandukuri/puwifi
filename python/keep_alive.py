import copy, loginpu,sys
from loginpu import ping_host as ph
from loginpu import ping_internet as pi
from signal import signal, SIGINT
from sys import exit
from time import sleep

"""
Accept user input and pass it to the loginpu module
    script <username> <password>
        url is set to deafault value http://10.0.0.11:8090/login.xml        
"""

def basic_login_nosys(username, password):
    x=0
    """
    Accept user input and pass it to the loginpu module
        main.py <username> <password>
            url is set to deafault value http://10.0.0.11:8090/login.xml        
    """
    url = "http://10.0.0.11:8090/login.xml"

    response = copy.deepcopy(loginpu.login(url, username, password)[:])
    return [response]

def keep_alive(username=sys.argv[1], password=sys.argv[2],interval=5): # 5 is suggested
    """
    Runs script forever to keep wifi connected logged in
    """

    if (ph):
        print("Check: Wifi HOST Alive")
    else:
        if ph == 2:
            print("Check: Recived OS error")
            exit(1)  
    # Loop

    if (pi):
        print("Check: Internet Access available")
        sleep(interval)
    else:
        print("Trying to Login")
        basic_login_nosys(username, password)

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