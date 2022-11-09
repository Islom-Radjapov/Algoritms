from Data import data_int
from datetime import datetime as date

def linear_search(list, param):
    start = date.now().time()
    for item in list:
        if item == param:
            end = date.now().time()
            print(f"Search completed in {end.second - start.second} minutes {end.microsecond - start.microsecond }")

            return item
    return "param not found"

print( linear_search(data_int, 999999) )