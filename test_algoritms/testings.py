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
    [x + 5 for x in range(99999999)]
    end = date.now().time()
    print(f"Search completed in {end.second - start.second} seconds {end.microsecond - start.microsecond} microseconds")


test()