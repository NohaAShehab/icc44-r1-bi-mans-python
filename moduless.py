


# def askforInt(customized_message='please enter number'):
#     # when I call the function , ask user to enter number
#     while True:
#         num = input(customized_message)
#         if num.isdigit():
#             return  int(num)  # end the function
#         print("--- please enter valid number ---")
#
#
#
# num1 = askforInt()  # when this functions returns with result
# # save the result in num1 (global variable)
# print(num1, type(num1))

################################################

""" import data from package
    import packagename.modulename

"""

# import  bi.validators
#
# def sumnum(num1, num2):
#     if bi.validators.validateValidNum(num1) and bi.validators.validateValidNum(num2):
#         return num1 + num2
#     print("-- not valid numbers ")
#     return  False
#
#
# res = sumnum(3,"4")
# print(res)

""" name validator """
# import  bi.validators as numvalid
#
# def sumnum(num1, num2):
#     if numvalid.validateValidNum(num1)==True and numvalid.validateValidNum(num2):
#         return num1 + num2
#     print("-- not valid numbers ")
#     return  False

# res = sumnum(3,"4")
# print(res)



#############################3


name = "Ahmed"

if name:  # bool(name)==True
    print("hi")
else:
    print("bye")


"""
    if expression respresents true --> do something 
"""









# import  bi.validators as myvalidator
#
# v = myvalidator.validateValidNum("iti")
#
# if myvalidator.validateValidNum("iti")==False:
#     print("not valid")
#
# if not myvalidator.validateValidNum("test"):
#     print("-----")

""" import part of the module from inside the package """

# from bi.validators import validateValidNum
# print(validateValidNum(10))


# import  iti
#
# iti.sayhello("Ahmed")

###########################
# from iti.greetings import saywelcome
# import  iti.greetings

# iti.greetings.saywelcome("Noha")

import  iti

iti.saywelcome("Ahmed")

import iti.greetings
iti.greetings.saywelcome("ggggg")