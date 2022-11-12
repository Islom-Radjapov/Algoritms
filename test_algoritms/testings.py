from datetime import datetime as date

def numJewelsInStones( jewels, stones):
    start = date.now().time()
    print( start.microsecond)
    result = 0
    for x in jewels:
        for y in stones:
            if x == y:
                result += 1
    end = date.now().time()
    print( f"Search completed in {end.second - start.second} seconds {end.microsecond - start.microsecond} microseconds" )
    return result

jewels = "aA"
stones = "aAAbbbb"


print(numJewelsInStones(jewels, stones))