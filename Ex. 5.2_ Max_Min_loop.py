largest = None
smallest = None


while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try :
        ival = int(num)
        if largest is None or ival > largest : largest = ival
        if smallest is None or ival < smallest : smallest = ival

    except :
        print("Invalid input")


print("Maximum is", largest)
print("Minimum is", smallest)
