fruitlist = []
listwithdata = ['a', 1, True, "Bob"]

#### Basic

fruitlist.append("apple")
fruitlist.extend(["Orange", "banana", "melon"])
print (fruitlist)

fruitlist.insert(2, "grape")
print (fruitlist)

#### Searching

print ("pear" in fruitlist)
print ("grape" in fruitlist)
print (fruitlist.index("banana"))

### modify

fruitlist[3] = "mango"
print(fruitlist)

### delete

fruitlist.remove("melon")
print(fruitlist)

#### CLEAR
fruitlist.clear()
print(fruitlist)

#### list builder

chars = list("abcdfdfghd")
print (chars)

nums = list(range(10, 200, 2))
print (nums)