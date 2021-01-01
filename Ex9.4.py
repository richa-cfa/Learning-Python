fname = input("Enter file name: ")
fh = open(fname)


dct =dict()

for line in fh:
    if not line.startswith("From:"): continue
    line_split = line.split()
    email = line_split[1]
    dct[email] = dct.get(email,0)+ 1

most = None
sender = None

for key in dct :
    if most is None or dct[key] > most :
        most = dct[key]
        sender = key


print(sender, most)
