import os
import sys
import time
os.system("clear")

def install():
 os.system("pkg install python -y")
 os.system("pkg install python2 -y")
 os.system("pkg install python3 -y")
 os.system("pkg install git -y")
 os.system("pkg install wget -y")
 os.system("pkg install figlet -y")
 os.system("pkg install ruby -y")
 os.system("pkg install php -y")
 os.system("pkg install clang -y")
 os.system("ggam install lolcat")
 os.system("pkg install proot-distro -y")
 print(" [✓] ALL PACKAGE ININSTALLED SUCCESSFULLY")
 
logo="""

███████╗██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ 
██╔════╝██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗
███████╗███████║███████║██╔██╗ ██║   ██║   ██║   ██║
╚════██║██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║
███████║██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ 
                                                    

 ╔════════════════════════╗
 # [✓] AUTHOR :Shanto       #
 # [✓] TOOL   :PKG INSTALL  #
 # [✓] VERSION:1.0          #
 # [✓] STATUS :WORKING      #
 ╚════════════════════════╝
"""
print (logo)

import getpass

attemps = 0

while attemps < 12345677901:
    username = input('Enter username: ')
    password = input('Enter password: ')

    if username == 'SHANTO' and password == 'shanto':
        print('You have successfully logged in.')
        break
    else:
        print('Incorrect Please Trying ')
        attemps += 1
        continue
os.system('clear')
print (logo)

per=input("Start Installation... (y/n)")
per=per.replace(" ","")
yes=("y","Y")
if per in yes:
  install()
elif per=="n":
  print("STOPED BY YOUR WISHES")
else:
  print("YOUR OPTIONS IS WRONG")
  sys.exit()
  print (welcome)
  




  