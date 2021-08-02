valid = False
while not valid:
    
    error = "please enter a number that is more than zero bro"

    try:
    
    
        response = float(input("enter a number"))


        if response > 0:
            valid = True


        else:
            print(error)
            print()
            
    except ValueError:
        print(error)