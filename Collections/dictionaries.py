from tkinter import filedialog


fileDesc = {}

nums = {1 : "one", 2 : "two", 3 : "three"}

# add values
fileDesc["pdf"] = "Portable Document Format"
fileDesc["txt"] = "Text file"
fileDesc["jpg"] = "JPEG image"

print(f"dictionay contains {len(fileDesc)} items")

print (fileDesc["jpg"])
fileDesc["jpg"] = "JPG"

print("txt" in fileDesc.keys()) #check for key
print("JPG" in fileDesc.values()) #check for values

del fileDesc["pdf"]
print (fileDesc)

fileDesc.clear()
print (fileDesc)

