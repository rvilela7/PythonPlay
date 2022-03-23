
def myFunction(arg1, arg2, *, suppressExceptions=False): #* Requires the next parameters to be named in Params
    print (arg1, arg2, suppressExceptions)

myFunction(1, 2, suppressExceptions=True) #Requires name param