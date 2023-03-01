# BITS WiFi Auto Login
Script for automating the login process for BITS Student WiFi

## How to use this script:
Firstly, clone this repo and navigate to it
```
 $ git clone https://github.com/ameya-deshmukh/BITSWifi-Auto-Login
 $ cd BITSWifi-Auto-Login/
 
```
Now, install the requirements by running this command:
```
$ python3 -m pip install requirements

```
Now, use your favourite code/text editor to edit script.py according to your username and password

After this, edit the 'bitslogin' file to include the path where you've cloned the repo

Then make the 'bitslogin' script executable by typing in:
```
$ chmod +x bitslogin

```
Then, add it to your PATH:
```
$ sudo cp bitslogin /usr/local/bin

```
Enjoy! Type in:
```
$ bitslogin

```
everytime you need to connect to BITS Wi-Fi and authenticate your credentials.
