from datetime import datetime as date
import numpy as np

def test():

    # test 1
    start = date.now().time()
    for x in range(99999999):
        x + 5
    end = date.now().time()
    print( f"Search completed in {end.second - start.second} seconds {end.microsecond - start.microsecond} microseconds" )

    # test 2
    start = date.now().time()
    [x + 5 for x in range(99999999)].count()

    end = date.now().time()
    print(f"Search completed in {end.second - start.second} seconds {end.microsecond - start.microsecond} microseconds")


# test()

def my_strlen(param_1):
    x = 0
    try:
        while param_1[x] != 0:
            x += 1
        return x
    except:
        return x

# print( my_strlen("RaInB0w d4Sh!") )



def my_strrchr(param_1, param_2):
    x = len(param_1) - 1
    while x > 0:
        if param_1[x] == param_2:
            return param_1[x:]
        x -= 1


# print( my_strrchr("abcabc", "b") )
#
# print( my_strrchr( "121212", "2") )
#
# print( my_strrchr("abc", "d" ) )
param8 = ["xoxAoxo", "xoxAox", "oxAox", "oxo", "A", "ooxAoxx", "oxooxo", "Axo"]
def str_maxlenoc(p1, p2):
    res1 = 0
    for x in p1:
        for y in x:
            if y in x:
                continue
            else:
                break
        res1 += 1
    return res1

# print( str_maxlenoc(["xoxAoxo", "xoxAox", "oxAox"],  3) )
#
# print( str_maxlenoc(param8, 8) )
#
#
# print( param8[0].split()[0] in param8[1].split() )


def isPerfectSquare(num):
    a = num ** 0.5
    print( a )
    print(a % 1 )
    print( np.sqrt(num) )
    return (num ** 0.5) % 1 == 0

print( "return=>", isPerfectSquare(14) )