from multiprocessing.sharedctypes import Value


try:
    a = 4  / 0
except ZeroDivisionError as e:
    print ("exception 2: ", e)
except:
    print ("exception 1")
finally:
    print ("end")


try:
    raise ValueError("cannot go further")
except BaseException as e: # !! as
    print ("Raised error", e)

