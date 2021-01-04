score = input("Enter Score:")
try:
    fval = float(score)
except:
    print("Error: Print only number within range 0-1")
    quit()

if fval>1 :
    print("Error: Print number within range 0-1")
elif fval<0 :
    print("Error: Print number within range 0-1")
elif fval >= 0.9 :
    print("A")
elif fval >= 0.8 :
    print("B")
elif fval >= 0.7 :
    print("C")
elif fval >= 0.6 :
    print("D")
else :
    print("F")
