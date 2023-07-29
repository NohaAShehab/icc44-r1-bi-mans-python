
# unlabeled data
info  = ["noha", 31, "iti", "phd student", "mansoura"]

""" dictionary 

    --> comma seperated key:value pair
    --> use keys instead of indices --> to access elements
    ==> doesn't allow key duplication 
    from 3.7 ---> sorted datatype
    
"""

"1- define dict "

d = {}
myd = dict()

"dict can hold different data from different datatypes"

myinfo = {"fname":"noha","age": 31,"work": "iti", "status":"phd student",
          "city":"mansoura", 1:10}

""" access elements using key """
print(myinfo["fname"])
""" modify dict elements """
myinfo["fname"] = "Noha"

myinfo["courses"]="python" # if key doesn't exists  --> add new key:value pair


print(myinfo)

"check no of key:value pairs in dict ? "
print(len(myinfo))

""" loop over the dict > """

# for item in myinfo:
#     print(f"item={item}")

# for item in myinfo:
#     print(f"item={item}, {myinfo[item]}")
" get keys, values "
keys_values = myinfo.items()
print(keys_values) # dict_items

# print(keys_values[0]) 'dict_items' object is not subscriptable
keys_values = list(keys_values)
#
# for k , v in myinfo.items():
#     print(f'{k}:{v}')
#

"get keys of the dict ? "

# keys = myinfo.keys()  #dict_keys -->  is not subscriptable object
# print(keys)
# keys= list(keys)


dvalues = myinfo.values()  #dict_values -->  is not subscriptable object
print(dvalues)
dvalues= list(dvalues)


"check if value exists in a dict"
print("Noha" in myinfo)  # check if value exists in the keys
print("Noha" in myinfo.values())

""" contcat dict ? """
additionalinfo ={"city":"Cairo", "street":"Abass"}
# all_info= additionalinfo + myinfo #TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
#
# print(all_info)

"update info"
print(myinfo)
myinfo.update(additionalinfo)
print(myinfo)
""" if you updating with exisiting key --> update the value ,otherwise ---> add new key:value"""



"casting dict ? to list / tuple / set "

info = list(myinfo)
print(info)


# myinfo.clear()
# print(myinfo)
#
# info.clear()
# print(info)

############
""" pop element from dict """

popped_value=myinfo.pop("fname")
print(popped_value)
print(myinfo)





