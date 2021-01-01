fname = input('Enter file name: ')
fh = open(fname)


total = 0
import re

#for line in fh:
#    y = re.findall('[0-9]+', line)
#    if len(y)>0 :
#        for num in y:
#            total = total + int(num)


#print(sum)

#1. shortcut


#y = re.findall('[0-9]+', fh.read())
#for num in y : total = total + int(num)

#print(sum)

#2. even shorter

print(sum([int(num) for num in re.findall('[0-9]+', fh.read())]))
