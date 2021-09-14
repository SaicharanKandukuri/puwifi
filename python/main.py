import loginpu, sys, copy, ssl
from urllib.parse import quote

"""
    Accept user input and pass it to the loginpu module
        main.py <url> <username> <password>
"""
username = sys.argv[1]
password = sys.argv[2]
url = "http://10.0.0.11:8090/login.xml"

response = copy.deepcopy(loginpu.login(url, username, password)[:])
if ( response[0] == True ):
    print("Successfully logged in as", username)
else:
    print("Failed to login")
    print("Response: "+ str(response))
