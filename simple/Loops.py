'''Loop playground'''

# TODO: Example 1
from tracemalloc import start


for i in range(-5, 5, 2):
    print (i, end=" :-) ")
print ("\n------")

# TODO: Example 2
for i in range(10):
    print (i)
print ("\n------")
# TODO: Example 3
for i in range(100, 1000, 100):
    print (i, end=" * ")
print ("\n------")

# TODO: Example 4
myString = "Rui Vilela"

for c in myString:
    print (c, end=",")
print ("\n------")

# TODO: Example 5
myString = "Dados numéricos"

print (myString)
for i, c in enumerate(myString):
    print (f"{str(i)}:{c}", end = " | ")

print ("\n---------")
# TODO: Example 6

KeepGoing = True
i = 0
z = 1
r = 0
while (KeepGoing):
    print (r, end = " ")
    r = i + z
    i = z
    z = r
    break
    if i > pow(2, 100):
        KeepGoing = False # or break

# 0 1 2 3 5 