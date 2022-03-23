def myfunc():
    print ("This is a line function")
    return 42

def myvoidfunc(a, b):
    print (a+b);

"""can contain multiple params"""
def variableargs(a, b, *args): 
    print(a+b)
    for arg in args:
        print (arg)

print (myfunc())

o = myvoidfunc (10, 5)
print (o)

variableargs(3, 4, "Rui", "bb", o, 33, 44.3)