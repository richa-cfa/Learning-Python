fname = input("Enter filename: ")
fh = open(fname)

di = dict()

for line in fh:
    temp = line.split()
    for word in temp :
        di[word] = di.get(word,0)+1

# the above code can be presented in 1 single line:
#make a list of lists using items()
#sort this list

how_many = int(input("Enter How many words:  "))

print(sorted([(v,k) for k,v in di.items()])[:how_many])
