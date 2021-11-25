import requests
# Basic example script
url = 'http://10.0.0.11:8090/login.xml'

headers = {
    "Host": "10.0.0.11:8090",
    "Content-Length": "77",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "*/*",
    "Origin": "http://10.0.0.11:8090",
    "Referer": "http://10.0.0.11:8090/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "close",
}
body = 'mode=191&username=test1&password=passurlencoded&a=1630404423764&producttype=0'
data = bytearray(body, 'utf-8')
r = requests.post(url, data=data, headers=headers, verify=False)
print(r.status_code)
print(r.text)
