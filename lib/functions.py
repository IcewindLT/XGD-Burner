#!/usr/bin/env python
# -*- coding: utf-8 -*-
encoding = 'utf-8'

import os, sys

def burn(DTYPE):
    if DTYPE == "xgd3":
        print("Burning INAME as DTYPE with layerbreak 2133520")
        os.system("growisofs -use-the-force-luke=dao -use-the-force-luke=break:2133520 -speed=2 -Z DVD=INAME")
        print("Done! You can now remove the disc..")
    elif DTYPE == "xgd2":
        print("Burning INAME as DTYPE with layerbreak 1913760")
        os.system("growisofs -use-the-force-luke=dao -use-the-force-luke=dao -use-the-force-luke=break:1913760 -dvd-compat -speed=2 -Z DVD=INAME")
        print("Done! You can now remove the disc..")
    elif DTYPE == "xgd3trunc":
        print("Burning INAME as DTYPE with layerbreak 2086912")
        os.system("growisofs -use-the-force-luke=dao -use-the-force-luke=break:2086912 -dvd-compat -speed=2 -Z DVD=INAME")
        print("Done! You can now remove the disc..")
    else:
        print("Something went wrong... Closing")
        sys.exit()
    return

def depcheck():
    if ( os.path.isfile('/usr/bin/growisofs')) == False:
        print("You need to have growisofs installed on your system to run this program..")
        sys.exit()
    elif ( os.path.isfile('/usr/bin/growisofs')):
        print("growisofs found... Starting XGDBurner..")
    return

def truncate():
    os.system("truncate --size=8547991552 INAME")
    return
