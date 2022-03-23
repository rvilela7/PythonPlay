data = [10, 6, 15, 23, 56, 64, 23, 232, 4, 2, 60]

print ("Sorted:")
result = sorted(data) #sorted from python
print (result)

print ("Sort by first data")
result = sorted(data, key=lambda x: str(x)[0])
print (result)