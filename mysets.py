
"""
    sets --> remove duplicates  # save elemensts in the sets  --> hashed elements
    ===> unsorted datatype
"""
"1- define a set "
ss = set()
myset = {"python", "bi", "sql","databases", "happy", 2023, 39, "iti", "python"}
print(myset)

ss = {2,40, -14, 20, -1000}

print(ss)

""" set can hold a list ? """
# ss = {"test", [3,4,-19]} # unhashable type: 'list'

""" get len of set """
print(len(ss))

""" add element to the set """

ss.add("added element")
# print(ss)


""" pop element """
# popped_element = ss.pop() # pop element from the set randomly
# print(popped_element)
#
# """ remove element : """
# ss.remove(2)


"check if element exists in the set "

print(2 in ss)


"enumrate and sets"

for index, item in enumerate(myset):
    print(f"index={index}, item= {item}")



""" cast sets to list/ tuple  """