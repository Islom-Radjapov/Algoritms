from Data import data_int
from datetime import datetime as date

def linear_search(list, param):
    start = date.now().time()
    for item in list:
        if item == param:
            end = date.now().time()
            return f"Search completed in {end.second - start.second} seconds {end.microsecond - start.microsecond } microseconds"
    return None
print( linear_search(data_int, 999_999) )