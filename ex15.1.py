import sqlite3
import re

fname = input('Enter file name: ')
#if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    domain = pieces[1].split('@')[1]
    print(pieces[1], domain)
    #domain = re.findall('.*@(*)', pieces[1])
    #print(domain)
