
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]
daysdict = {"Sun": "Dim", "Mon": "Lun", "Tue": "Mar",
            "Wed": "Mer", "Thu": "Jeu", "Fri": "Ven", "Sat": "Sam"}

# TODO: iterate over a list
print("using iter:")

i = iter(days)
print (next(i))
print (next(i))
print (next(i))

# TODO: iterate over a dictionary
print("dictionary iteration:")
for key in daysdict:
    print (key, ":", daysdict[key])

print("\n---------\n")

for k,v in daysdict.items():
    print(k, v)

# TODO: use the enumerate function
print("using enumerate:")

for i,m in enumerate(days, start=5):
    print (i,m)

# TODO: use the zip function
print("using zip:")
for m in zip(days, daysFr):
    print (m)

# TODO: combine enumerate and zip
print("using enumerate with zip:")
for i, m in enumerate(zip(days, daysFr), start=1):
    print (f"Day {i}, {m[0]} is {m[1]} in french")

