fname = input("Enter File name: ")
fh = open(fname)

di = dict()
lst = list()

for line in fh:
    if line.startswith('From ') :
        lst = line.split()
        time = lst[5]
        hour = time[:2]
        di[hour] = di.get(hour,0)+1
    continue


lst = sorted([(k,v) for k,v in di.items()])

for k,v in lst:
    print(k,v)
