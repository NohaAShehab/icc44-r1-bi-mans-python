

""" math module """
# import  math
#
# print(math.pi)  # act like constant
#
# print(math.cos(.5))
# print(math.ceil(55.6))
# print(math.ceil(55.4))
# print(round(4.4))
# print(round(4.6))


###
import datetime

print(datetime.date(2023,7,31))

import  time
print(time.time())  # time --> unix timestamp


# import  os
# print(os.getcwd())
#
# os.mkdir("bimans")


#### regex  --> regular expressions


""" define pattern ---> extract text from file 

    import re
    
    out=re.match(pattern, string)
    if out --> None --> string doen't match the pattern 
    else --> match object ---> 
    

"""

# name = input("please enter name: ") ## name consists of chars only -don't isalpha-


# 1- import re module
import re
# pattern = r"[A-Z]"
#
# res=re.match(pattern, name)  # return with match object if part of the string follow pattern
# print(res)


### Noha--> None

# pattern = r"[A-Z]*"
#
# res=re.fullmatch(pattern, name)  # return with match object if all the string parts follow pattern
# print(res)


### validate salary
# sal = input("please enter number ")
# numpattern=r'[0-9]{5}'
# if re.fullmatch(numpattern, sal):
#     print("valid number")
#
# else:
#     print("--- not valid ")


"87878-39999"