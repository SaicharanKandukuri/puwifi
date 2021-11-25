# python3
import sys
import urllib
import requests

################################################################
# Basic usage of loginpu.py as module
#
# Copyright (C) 2021 SaicharanKandukrui <saicharankandukuri1x1@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
###################################################################

"""
essentials to login to parul wifi
Copyright (C) 2021 SaicharanKandukrui <saicharankandukuri1x1@gmail.com>
"""


def login(login_url="http://10.0.0.11:8090/login.xml", username=None, password=None):
    """
    Sends Login requests to Parul University Login Page
    """
    url = str(login_url)

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
    body = 'mode=191&username=' + username + '&password=' + \
        password + '&a=1630404423764&producttype=0'
    data = bytearray(body, 'utf-8')  # server takes header body data in binary
    r = requests.post(url, data=data, headers=headers, verify=False)
    return [(r.status_code == 200), r.text, r.status_code]
