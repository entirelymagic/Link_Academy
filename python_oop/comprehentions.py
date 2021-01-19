some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

# create a list of uniq items that repeat in a list
duplicates_02 = list({x for x in some_list if some_list.count(x) > 1})

print(duplicates_02)
