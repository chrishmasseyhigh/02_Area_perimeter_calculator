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
print ()
print ("width", width)
print ("hight", hight)
print ()
