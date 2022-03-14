'''Sample program to check vars syntax'''

f = 100
print(f)
b = True
print (b)
z = "abdfgf"
print (z)

print (f"{f} {b} {z}");

# TODO: Using str to 
print (str(f) + ' ' + str(b)); 

###

print (f)

def somefunction():
    global f 
    f="show me a variable in a function"
    print(f)

somefunction()
print (f)
# del f
# print (f)