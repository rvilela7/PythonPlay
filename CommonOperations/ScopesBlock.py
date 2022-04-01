with open("fileSample.txt") as fic: #from params?
    lineCount = 0
    while True:
        myLine = fic.readline()
        myLine = myLine.strip() # eol strip
        if not myLine:
            break
        print (myLine)
        lineCount += 1
    
    print (f"The file has {lineCount} lines")

