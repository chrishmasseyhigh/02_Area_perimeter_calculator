# functions go here

#checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:
        
        error = "please enter a number that is more than zero bro"

        try:
        

            response = float(input(question))


            if response > 0:
                return response


            else:
                print(error)
                print()
                
        except ValueError:
            print(error)


#main rotine goes here
width = num_check("width: ")
hight = num_check("hight: ")




#calculate area (width times hight)
area = width * hight

#calculate perimeter (width plus hight) * 2
perimeter = 2 * (width + hight)

print ("Perimeter: {} units" .format(perimeter))
print ("area: {} square units" .format(area))