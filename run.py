
import os
import time
import sys

os.system("clear")

def slowprint1(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 100)
slowprint1('''\033[91m

      ___          ___          ___             ___ 
     /\  \        /\  \        /\  \  ___      /\__\
    /::\  \      /::\  \       \:\  \/\  \    /::|  |
   /:/\ \  \    /:/\:\  \  ___ /::\__\:\  \  /:|:|  |
  _\:\~\ \  \  /::\~\:\  \/\  /:/\/__/::\__\/:/|:|__|__
 /\ \:\ \ \__\/:/\:\ \:\__\:\/:/  /_/:/\/__/:/ |::::\__\
 \:\ \:\ \/__/\/__\:\/:/  /\::/  /\/:/  /  \/__/~~/:/  /
  \:\ \:\__\       \::/  /  \/__/\::/__/         /:/  /
   \:\/:/  /       /:/  /         \:\__\        /:/  /
    \::/  /       /:/  /           \/__/       /:/  /
     \/__/        \/__/                        \/__/
        CREATE BY SAJIM
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)
print (''' \033[95m
+--------------------------------------+
| This Tool Install All Basic Packages |
+--------------------------------------+
| Coded By Sajim | version 2.1|
+--------------------------------------+''')

slowprint(''' \033[93m
[01] python
[02] python2
[03] python-dev
[04] python3
[05] php
[06] java
[07] git
[08] perl
[09] bash
[10] nano
[11] curl
[12] openssl
[13] openssh
[14] wget
[15] clang
[16] nmap
[17] w3m
[18] hydra
[19] ruby
[20] macchanger
[21] host
[22] dnsutils
[23] coreutils ''')
slowprint('''\033[96m
This Command for access Storage in Termux
[00] termux-setup-storage''')
print ("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update")
os.system ("apt upgrade -y")
slowprint('''\033[93m WAIT FOR NEXT...create by sajim''')
os.system ("apt install python -y")
slowprint('''\033[96m WAIT FOR NEXT...create by sajim''')
os.system ("apt install python2 -y")
slowprint('''\033[93m WAIT FOR NEXT...create by sajim''')
os.system ("apt install php -y")
slowprint('''\033[96m WAIT FOR NEXT...create by sajim''')
os.system ("apt install python-dev -y")
slowprint('''\033[93m WAIT FOR NEXT...create by sajim''')
os.system ("apt install python3 -y")
slowprint('''\033[96m WAIT FOR NEXT...create by sajim''')
os.system ("apt install java -y")
slowprint('''\033[93m WAIT FOR NEXT...create by sajim''')
os.system ("apt install git -y")
slowprint('''\033[96m WAIT FOR NEXT...create by sajim''')
os.system ("apt install perl -y")
slowprint('''\033[93m WAIT FOR NEXT...create by sajim''')
os.system ("apt install bash")
slowprint('''\033[96m WAIT FOR NEXT...create by sajim''')
os.system ("apt install nano -y")
slowprint('''\033[96m WAIT FOR NEXT...create by sajim''')
os.system ("apt install curl -y")
slowprint('''\033[93m WAIT FOR NEXT...create by sajim''')
os.system ("apt install openssl -y")
slowprint('''\033[96mWAIT FOR NEXT...create by sajim''')
os.system ("apt install openssh -y")
slowprint('''\33[93m WAIT FOR NEXT...create by sajim''')
os.system ("apt install wget -y")
slowprint('''\033[96m WAIT FOR NEXT...create by sajim''')
os.system ("apt install clang -y")
slowprint('''\033[93m WAIT FOR NEXT...create by sajim''')
os.system ("apt install nmap -y")
slowprint('''\033[96m WAIT FOR NEXT...create by sajim''')
os.system ("apt install w3m -y")
slowprint('''\033[93m WAIT FOR NEXT...create by sajim''')
os.system ("apt install hydra -y")
slowprint('''\033[96m Insttaling hydra tool...create by sajim''')
os.system ("apt install ruby -y")
slowprint('''\033[93m WAIT FOR NEXT...create by sajim''')
os.system ("apt install macchanger -y")
slowprint('''\033[96m WAIT FOR NEXT...create by sajim''')
os.system ("apt install host -y")
slowprint('''\033[93m WAIT FOR NEXT...create by sajim''')
os.system ("apt install dnsutils -y")
slowprint('''\033[96m WAIT FOR NEXT...create by sajim''')
os.system ("apt install coreutils -y")
slowprint('''\033[93m ("Allow the Button For Access the Storage in Termux")''')

os.system ("termux-setup-storage")



def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
slowprint('''[ {All Compelete}
''')

input("\n\nPress the enter key to exit : ")
