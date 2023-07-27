# name = 'Ahmed' # define variable # detect datatype of variable in the runtime
# age = 27  # int
# city = 'Tanta'
# happy = True  # False
# print(city)
# print(name)
#
# print("hello world")

###########3 Don't do this

# and = 10

# num = 10
# happy = False
# print(num)
# print = 10
# print(happy)


"""
    if(){}


"""

happy = True

# if happy==True:
#     print("-- hi ---")
# else:
#     print("=--bye --")


# if happy==True:
# print("---hi")
#
#

# if happy == True:
#     print("--hi")
# else:
#     print("---bye ----")

################# strings

name = 'Ahmed'
track = "python"

## mutliline string
# bio = "My name is Noha" \
#       "I works at ITI"
#
# print(bio)


bio = """My name is Noha
I works at ITI"""

print(bio)



""" this is my string 
testg 
tesfeef
like a comment 
"""

year = 2023

# print type of varibale
# print(type(year))
#
# year = "2023"
# print(type(year))
######################################################
""" type casting  --> convert between different type in python """
""" convert int to string """
# num = 10
# print(type(num))
# num = str(num)  # casting cast int to string
# print(type(num))

"""convert string to int """
# string  is numeric string ? ---> consists only from digits from 0 - > 9
# num  ="10"
# print(type(num))
# num = int(num)
# print(num)
# print(type(num))
# print("--- convert string to int ----")
# name = 'noha'
# name = int(name)


"conver bool to string and vice versa "
# happy  = True
# happy = str(happy)
# print(happy)

# mood = 'True'
# mood = bool(mood)
# print(mood, type(mood))

# name= "noha"
# name = bool(name)
# print(name, type(name))
###

# print(True =="True")
# print(True ==bool("True"))

print(True is True)

# note is operator in python

################################################

print(10 and 3)

print("iti" and 10 and "python")

res  =10 and 3
print(type(res))  # when converted to bool --> True



if name:  # bool(name)
    print("hi")
else:
    print("bye ")


message = "                       "  # this not empty string
print(bool(message))
if message:
    print("hi")
else:
    print("bye")


# print(''==False)