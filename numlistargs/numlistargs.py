#!python3
# print integer numbers from N to M (accept --n and --m) 

import sys

num_start = 0
num_end = 0
arg_count = len(sys.argv)

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def commandLineError():
    print("\n Oh... It didn't work. \n I can accept only 2 integer arguments. \n Try this patten, please: <file name> <integer> <integer>\n Thank you for using our servise :) \n")

def toInteger(s):
    return int(s)
    
if arg_count == 3:

    if (isInt(sys.argv[1]) and isInt(sys.argv[2])):
        num_start = toInteger(sys.argv[1])
        num_end = toInteger(sys.argv[2])
        for i in range(num_start, num_end + 1):
            print(i)
    else:
        commandLineError()
else:
    commandLineError()