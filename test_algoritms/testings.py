from datetime import datetime as date

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


print( my_strrchr("abcabc", "b") )

print( my_strrchr( "121212", "2") )

print( my_strrchr("abc", "d" ) )