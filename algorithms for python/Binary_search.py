from Data import data_int
from datetime import datetime as date

def binary_search(list, param):
    start = date.now().time()
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == param:
            end = date.now().time()
            return f"Search completed in {end.second - start.second} seconds {end.microsecond - start.microsecond} microseconds"
        if guess > param:
            high = mid - 1
        else:
            low = mid + 1
    return None

print( binary_search(data_int, 3) )