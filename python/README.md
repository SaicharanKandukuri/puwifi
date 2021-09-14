# logmein python Version

python script to login parul university wifi

# usage

first cd to this directory then

## Normal One-Time Login
for this a template script is avalible `main.py`
take two command line arguments 
 1. username
 2. password

example:
```
python3 main.py 200303124264 idkmypassword
```

## forever login script

this one check access to internet with 5 seconds interval and log back in if wifi logged out

take two command line arguments 
 1. username
 2. password

```
python3 keep_alive.py 200303124264 iwontsaymypassowrd
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
    
    ping_host()
    
    ping_internet()

FILE
    /root/repos/logmein/python/loginpu.py
```
## loginpu.py
A library with essentials to login to parul wifi

functions

`login` → Sends Login requests to Parul University Login Page
take two arguments all are strings

usage:
```

```
> WIP