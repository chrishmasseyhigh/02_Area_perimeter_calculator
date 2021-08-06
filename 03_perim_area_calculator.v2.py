# functions go here

#checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:
        
        error = "please enter a number that is more than zero"

        error2 = "Please eneter a number"                                                                  
        try:
        

            response = float(input(question))


            if response > 0:
                return response


            else:
                print(error)
                print()
                
        except ValueError:
            print(error2)


#main rotine goes here

keep_going=""
while keep_going == "":

    width = num_check("width: ")
    hight = num_check("hight: ")




    #calculate area (width times hight)
    area = width * hight

    #calculate perimeter (width plus hight) * 2
    perimeter = 2 * (width + hight)

    print ("Perimeter: {:.2f} units" .format(perimeter))
    print ("area: {:.2f} square units" .format(area))

    keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("thanks for using the area / perimeter calculator")