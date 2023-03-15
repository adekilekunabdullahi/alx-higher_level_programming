def complex_delete(a_dictionary, value):
    b = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            b.append(key)
    for x in b:
        del a_dictionary[x]
    return a_dictionary
