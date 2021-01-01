fname = input("Enter file name: ")
fh = open(fname)


dct =dict()

for line in fh:
    if not line.startswith("From:"): continue
    line_split = line.split()
    email = line_split[1]
    dct[email] = dct.get(email,0)+ 1

value_list = list()


for k in dct:
    new = (dct[k],k)
    value_list.append(new)

value_list = sorted(value_list,reverse=True)

print(value_list[0])
