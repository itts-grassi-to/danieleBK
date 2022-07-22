#!/usr/bin/python3
import os
os.chdir("/opt/danieleBK")
from bkFile import bkFile
c=bkFile("infoschool.json","AXIOSDATABASE.FDB")
#c=bkFile("infoschool.json","pipi.txt")
if c.initOK:
    c.backuppa()
print("finito ho")
