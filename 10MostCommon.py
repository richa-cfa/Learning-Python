fname = input("Enter filename: ")
fh = open(fname)

di = dict()

for line in fh:
    temp = line.split()
    for word in temp :
        di[word] = di.get(word,0)+1


lst = list()

############################################################
# good example of how to use FOR instead of While
# when retriving information from LIST
how_many = int(input("How many top words do you want?: "))

req = 0

while req<how_many:
    print(lst[req])
    req = req+1

for val, key in lst[:how_many]:
    print(key, val)
############################################################


#





print("Done")
