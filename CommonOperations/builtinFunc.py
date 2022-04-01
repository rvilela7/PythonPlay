
a = ["fttdfg", "5", "gdfg"]

print (len(a))
print (min([5, 4, 5]))
print (max([5, 4, 5]))

# Max min applied to other range
print (max(a, key=lambda x: len(x) ))
print (min(a, key=lambda x: len(x) ))

print (sorted(a))
print (sorted(a, key=lambda x: len(x)))

# returns boolean types
print (any(len(w) < 3 for w in a))
print (all(x > 4 for x in list(range(1,10))))

