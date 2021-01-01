fname = input("Enter file name: ")
fh = open(fname)
count = 0

lst =list()

for line in fh:
    if not line.startswith("From:"): continue
    line_split = line.split()
    email = line_split[1]
    lst.append(email)
    print(email)
    count = count +1





print("There were", count, "lines in the file with From as the first word")
