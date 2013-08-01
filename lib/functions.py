#!/usr/bin/env python
import os

def burn(DTYPE):
    if DTYPE == xgd3:
        print("Burning INAME as DTYPE with layerbreak LAYERBREAK")
        os.system("growisofs -use-the-force-luke=notray -use-the-force-luke=break:2133520 -speed=SPEED -Z DVD=INAME")
        print("Done! You can now remove the disc..")
    elif DTYPE == xgd2:
        print("Burning INAME as DTYPE with layerbreak LAYERBREAK")
        os.system("growisofs -use-the-force-luke=notray -use-the-force-luke=dao -use-the-force-luke=break:1913760 -dvd-compat -speed=SPEED -Z DVD=INAME")
        print("Done! You can now remove the disc..")
    elif DTYPE == xgd3trunc:
        print("Burning INAME as DTYPE with layerbreak 2086912")
        os.system("growisofs -use-the-force-luke=dao -use-the-force-luke=break:2086912 -dvd-compat -speed=SPEED -Z DVD=INAME")
        print("Done! You can now remove the disc..")
    else:
        print("Something went wrong... Closing")
    return

def testarg(DTYPE):
    if DTYPE == None:
        print("You need to specify a disc type")
        print("EG: xgd2, xgd3, or xgd3trunc")
    if INAME == None:
        print("You have to specify an ISO file name and path")
        print("EG: /home/foo/Downloads/xboxgame.iso")
    return

def depcheck():
    if ( not os.path.isfile('/usr/bin/growisofs')):
        print("You need to have growisofs installed on your system to run this program..")
        exit
    elif ( os.path.isfile('/usr/bin/growisofs')):
        print("growisofs found... Starting XGDBurner..")
    return

def truncate():
    os.system("truncate --size=8547991552 INAME")
    return
