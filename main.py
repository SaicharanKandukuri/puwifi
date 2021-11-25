import loginpu
import sys
import copy
from loginpu import ping_host as ph

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
Accept user input and pass it to the loginpu module
    main.py <username> <password>
        url is set to deafault value http://10.0.0.11:8090/login.xml        
"""
username = sys.argv[1]
password = sys.argv[2]
url = "http://10.0.0.11:8090/login.xml"
response = copy.deepcopy(loginpu.login(url, username, password)[:])
if (response[0] == True):
    print("Successfully logged in as", username)
else:
    print("Failed to login")
    print("Response: " + str(response))
