import loginpu
from urllib.parse import quote

username = "200303124264"
password = "bf@66"
url = "http://10.0.0.11:8090/login.xml"

print(loginpu.send(url ,username, password)[:])
