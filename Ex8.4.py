fname = input("Enter file name: ")
fh = open(fname)

lst = list()

for line in fh:
  line_split = line.split()
  for w in line_split:
    if w not in lst: lst.append(w)

lst.sort()

print(lst)
