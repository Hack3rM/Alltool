import os

import time

print("do you went to start this tool[Y/n]" + "\n"  "[by default Y]")
name = input (">>")
if name == "Y" or name == "":
      os.system("pkg install wget")
      na_me = input ("""
             #####|     ######   ######
#     #     ##    |     #        #    #    #      #
 #   # #   # #### |     #        #    #   # #    # #
  # #   # #  #    |     #        #    #  #   #  #   #
   #     #   #### |____ #######  ###### #     #      #
        
 Select option

1.Metasplot Framework
2.nethunter on termux
3.keylogger
4.hidenEye
5.cupp
6.T-Header
[00]:exit
select no[..""")
if na_me == "1":
    print("##Installing metaspliot##" + "\n")
    os.system("wget https://github.com/gushmazuko/metasploit_in_termux.git")
    exit()
if na_me == "2":
    os.system("clear")
    print("##installing nethunter on termux##" + "\n")
    os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
    print("type ##chmod +x install-nethunter-termux")
    exit()
if na_me == "3":
    os.system("https://github.com/shivamsuyal/Android-Keylogger.git")
    exit()
if na_me == "4":
    os.system("https://github.com/Morsmalleo/HiddenEye.git")
    exit()
if na_me == "5":
    os.system("https://github.com/Mebus/cupp.git")
    exit()
if na_me == "6":
    print("installing T-Header")
    os.system("https://github.com/remo7777/T-Header.git")
if na_me == "00":
    os.system("clear")
    exit()b.com/remo7777/T-Header.git")
if na_me == "00":
    os.system("clear")
    exit()
