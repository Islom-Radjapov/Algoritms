from datetime import datetime as date

def numJewelsInStones( jewels, stones):
    start = date.now().time()
    result = 0
    for x in range(9999999):
        x
    end = date.now().time()
    print( f"Search completed in {end.second - start.second} seconds {end.microsecond - start.microsecond} microseconds" )

jewels = "aA"
stones = "aAAbbbb"


print(numJewelsInStones(jewels, stones))