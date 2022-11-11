from Data import data_confused

# Kopayib boruvchi tartiblash
def sort_asc(data):
    res = sorted(data)
    return res

# Pasayib boruvchi tartiblash
def sort_desc(data):
    res = sorted(data, reverse=True)
    return res


print(data_confused)
print(sort_asc(data_confused))
print(sort_desc(data_confused))