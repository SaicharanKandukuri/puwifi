# logmein python Version

python script to login parul university wifi

# usage
## Normal One-Time Login
for this a template script is avalible `main.py`
take two command line arguments 
 1. username
 2. password

example:
```cmd
python3 main.py username password
```

## forever login script
this one check access to internet with 5 seconds interval and log back in if wifi logged out

take two command line arguments 
 1. username
 2. password

```cmd
python3 keep_alive.py username password
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


