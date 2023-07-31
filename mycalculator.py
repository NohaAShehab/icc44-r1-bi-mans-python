

# def mycal():
#     ## ask user to enter 2 numbers
#     """ """
#     while True:
#         num1 = input("please enter num1 : ")
#         if num1.isdigit():
#             num1 = int(num1)
#             break
#         print("--- please enter valid number ---")
#
#     while True:
#         num2 = input("please enter num1 : ")
#         if num2.isdigit():
#             num2 = int(num2)
#         print("--- please enter valid number ---")

#######################################

#
# def askforInt(customized_message='please enter number'):
#     # when I call the function , ask user to enter number
#     while True:
#         num = input(customized_message)
#         if num.isdigit():
#             return  int(num)  # end the function
#         print("--- please enter valid number ---")
#
#
# def mycal():
#     num1= askforInt("please enter num1: ")
#     num2= askforInt("please enter num2: ")
#     res = num1 + num2
#     return  res
#







#################################################3

""" import external python module in your module
    you import functions and variables
"""
# import inputhelpers
# inputhelpers.askforInt("please enter age: ")

# print(inputhelpers.happy)
# def mycal():
#     ## to access content of the python module
#     # use modulename.functionname
#     num1= inputhelpers.askforInt("please enter num1: ")
#     num2= inputhelpers.askforInt("please enter num2: ")
#     res = num1 + num2
#     return  res


# myres = mycal()


### modify value of happy
#
# inputhelpers.happy = False

""" import part of the module 

    from modulename import specificpart
"""



# from inputhelpers import askforInt
#
# def mycal():
#     num1= askforInt("please enter num1: ")
#     num2= askforInt("please enter num2: ")
#     res = num1 + num2


""" alias the import """

from inputhelpers import askforInt as intnum

def mycal():
    num1= intnum("please enter num1: ")
    num2= intnum("please enter num2: ")
    res = num1 + num2





