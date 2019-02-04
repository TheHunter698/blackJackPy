#Recursioooooon :D

def ret_numbers_until_done():
    maximum = None
    minimum = None
    
    number = input('Number here:')
    
    if number == 'done':

        print(maximum, minimum)
        return 'done'
   	else:
           
        try:
            int(number)
            if maximum == None and minimum == None:
                maximum = number
                minimum = number
            elif number < minimum:
                minimum = number
           	elif number > maximum:
                maximum = number
      	except:
            print('Invalid input')
        
        return ret_numbers_until_done()
    