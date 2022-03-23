def namedparams (a, b, c=False):
    if c:
        print ("'a' comes first")
        print (a)
        print (b)
    else:
        print ("'b' comes first")
        print (b)
        print (a)

namedparams(5, b="Hello", c=True)
namedparams(10, b="World")