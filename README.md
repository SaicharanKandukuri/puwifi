# logmein python Version

> python script to login parul university wifi

![imageonline-co-roundcorner](https://user-images.githubusercontent.com/68287637/143475678-bc8c317c-3961-4f7f-bcfd-bfce190811b0.png)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSaicharanKandukuri%2Fpuwifi.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FSaicharanKandukuri%2Fpuwifi?ref=badge_shield)

# Installation
- make sure you installed python in your OS
```bash
git clone https://github.com/SaicharanKandukuri/puwifi
cd puwifi
pip install -r requirements.txt
```
# usage
## ❤️‍🔥 forever login script
this one check access to internet with 5 seconds interval and log back in if wifi logged out

take two command line arguments 
 1. username
 2. password

```cmd
python3 keep_alive.py username password
```

## 1️⃣ Normal One-Time Login
for this a template script is avalible `main.py`
take two command line arguments 
 1. username
 2. password

example:
```cmd
python3 main.py username password
```


<hr>

# Module


```
Help on module loginpu:

NAME
    loginpu

FUNCTIONS
    login(login_url='http://10.0.0.11:8090/login.xml', username=None, password=None)
        Sends Login requests to Parul University Login Page

FILE
    modules/loginpu.py
```
## loginpu.py
A library with essentials to login to parul wifi

functions

`login` → Sends Login requests to Parul University Login Page


# License
**Copyright (C) 2021 SaicharanKandukuri <saicharankandukuri1x1@gmail.com>**
> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.


[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSaicharanKandukuri%2Fpuwifi.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FSaicharanKandukuri%2Fpuwifi?ref=badge_large)