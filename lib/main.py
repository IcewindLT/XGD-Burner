#!/usr/bin/env python
# -*- coding: utf-8 -*-
encoding = 'utf-8'

import os, sys, functions, wx

print("XGD-Burner 0.1 beta")
print("Developer: DJYoshaBYD")

print("Please choose the ISO you want to burn..")
INAME = raw_input()
if INAME == "":
    print("You need to choose a type in the full path to the ISO you want to burn... Closing.")
    sys.exit()

print("Have you run the ISO through ABGX360? y/n")
abg = raw_input()
if abg == "n":
    print("You need to do that before we continue. Exiting...")
    sys.exit()

print("Checking ISO for size/type")
DSIZE = os.path.getsize(INAME)

if DSIZE > 8547991552:
    DTYPE="xgd3"
    print("This is an XGD3 disc. Some games do not work when truncated. Do you want to truncate? y/n")
    trunc = raw_input()
    if trunc == y:
        functions.truncate
        DTYPE="xgd3trunc"
    elif trunc == n:
        print("The disc will not work if you are not running an Lite-On iHAS Burner")
        print("Do you wish to continue? y/n")
        ihas = raw_input()
    if ihas == n:
        print("Please try agai with iHAS burner or use truncate AT YOUR OWN RISK")
        sys.exit()
elif DSIZE < 8547991552:
    DTYPE="xgd2"

print("Choose your DVD burner. You will need to put /dev/ in front of the drive name")
os.system("echo dmesg | egrep -i --color 'cdrom|dvd|cd/rw|writer'")
DVD = raw_input()

