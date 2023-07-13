# PU-wifi
A python program that simulates [parul university](https://www.google.com/search?q=parul+university) wifi web authentication request process to keep you device connected to parul university wifi (with-a-loop)

![image](https://user-images.githubusercontent.com/68287637/146675073-7e1aebcc-056d-4351-b5aa-f7e2f57b1853.png)

<!--
![image](https://user-images.githubusercontent.com/68287637/146674599-1568723d-6c70-49e8-8d71-1275ab3b169d.png)
-->


[![CodeQL](https://github.com/SaicharanKandukuri/puwifi/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/SaicharanKandukuri/puwifi/actions/workflows/codeql-analysis.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/saicharankandukuri/puwifi/badge)](https://www.codefactor.io/repository/github/saicharankandukuri/puwifi)
[![Pylint](https://github.com/SaicharanKandukuri/puwifi/actions/workflows/pylint.yml/badge.svg)](https://github.com/SaicharanKandukuri/puwifi/actions/workflows/pylint.yml)

- supported OS: `Linux`, `Windows`, `MacOS` and `Android` (with `Termux`)
- supported python versions: `python3.6` and above


## Installation

### with `pip`

- make sure you installed `python` and `pip` in your OS

```bash
pip install puwifi
```

## Usage

#### General

##### ♾️ Forever login mode `-k`
this is what the aim of repo

`-k` or `--keep-alive` attribute is say script to run a forever loop!
> scripts tries to contact `google.com` if connection fails script tries to send login request to host *i.e: 10.0.0.1* with username & password provied with `-u` & `-p` arguments


```bash
puwifi -k -u YOUR_USERNAME -p YOUR_PASSWORD 
```

##### 🪵 One-time login `-l`
you can login with `-l` or `--login` argument

```bash
puwifi -l -u YOUR_USERNAME -p YOUR_PASSWORD
```
##### 💥 Logout from puwifi
for logout use option `-o` or `--logout` argument
```bash
puwifi -o -u YOUR_USERNAME -p YOUR_PASSWORD 
```

<!--
> idk why logout requires username and password too! ( vunerability ? )
--> 

<hr>

## Finally
This repo is made fully on self-intrest cause iam a student in parul university, wifi here is `great&fast` but a bit tricky
![RepeatJumpGIF](https://user-images.githubusercontent.com/68287637/146674165-5d586b3c-dfce-41d7-8ebe-54917b27fb91.gif)

so instead of playing dino i made this script by re-enginerring an year old puwifi login website & used some of knowledge to make this script happen

### follow me on

- 😺 [github](https://github.com/SaicharanKandukuri), 

- 🦜 [Twitter](https://twitter.com/AtonZman1x1)

- 📸 follow me on Instagram: `atonzman1x1`

- 🎮 Add me on discord: `SAICHARAN KANDUKURI#3741`

🌟 If this work of me helped you make sure you start this repo, or buy me a juice of coffee when we meet 🥤


> ⚠️ Dont use practices used in this code for any kind of mischievous things. i need wifi working
>

![PusheenCatGIF](https://user-images.githubusercontent.com/68287637/146673862-cdb4f86e-c55b-470e-aa3f-b98dd362c6fb.gif)
###### go watch your videos now


<hr>

###### (©️) MIT License @SaicharanKandukuri 

