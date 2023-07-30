# user defined functions
""" functions with known number of arguments """
# function special variable

# 1- define function
"""
    def functionname(arguments):
        body of the function # maximum 20 line
        return [value or set values ]

"""
# def sayGoodmorning():
#     pass
#
# # 2- calling the function
# sayGoodmorning()

"""functions that do specific operation """

# def sayGoodmorning():
#     print("---- Good Morning BI Mansoura <3 -----")
#
#
# sayGoodmorning()
# res = sayGoodmorning()  # None object
""
# def sayGoodmorning():
#     print("---- Good Morning BI Mansoura <3 -----")
#     return
#
#
# sayGoodmorning()
# res = sayGoodmorning()  # None object

"""function accept arguments """

# def printfullname(fname, lname):
#     fullname=  f"{fname} {lname}".title()
#     print(fullname)
#     return  fullname
#
# printfullname('noha', 'shehab')

""" -----------> functions and arguments datatypes -----------"""

# def sumnums(num1, num2):
#     res= num1 + num2
#     print(res)
#
# sumnums(3,4)
# sumnums("iti", "test")
#
#

# def sumnums(num1, num2):
#     if num1.isdigit() and num2.isdigit():
#         res= int(num1) + int(num2)
#         print(res)

# sumnums(3,4)
# sumnums("iti", "test")

""" restrict the arguments types """


# def sumnums(num1: int, num2: int) -> None:  # for developer usage # documentation
#     res = num1 + num2
#     print(res)
#
#
# sumnums(4,5)
# sumnums("Ahmed", "Ali")
# sumnums("Ali", 455)

######################################33

#
# def sumnums(num1: int, num2: int) -> None:  # for developer usage # documentation
#     if isinstance(num1, int) and isinstance(num2, int):
#         res = num1 + num2
#         print(res)
#
#     else:
#         print("=-- not valid function parameter ")
#
#
# sumnums(4,5)
# sumnums("Ahmed", "Ali")
# sumnums("Ali", 455)


################################################33
""" functions with default arguments """
""" 
    non default arguments must preced default arguments
"""

# def mulnums(num1 :int =1, num2:int=1 ) ->float:
#     print(f"num1={num1}, num2={num2}")
#     if isinstance(num1, int) and isinstance(num2, int):
#         res = num1 * num2
#         return  res
#     print("---- not valid arguments ")
#
#
# res=mulnums(3)
# mulnums()
# res2= mulnums(5,2)


# def sumnum(num1, num2):  # num1, num2 are mandatory arguments to call function
#     res = num1 + num2
#
# sumnum(4,56)

# def sumnum(num1, num2=1):  # num1, num2 are optional arguments to call function
#     res = num1 + num2
#
#
# sumnum(4, 56)

""" functions with unknown number of arguments """

print(4,5,6,6,7,7,7,4)
print()


""" function that accepts zero or more arguments """

# def askfordrink(*drinks): # * --> function accepts zero or more arguments
#     print(drinks)  # tuple
#
# askfordrink("tea", "coffee", "water", "orange juice")
# askfordrink()
#
#
# print('hi', end='  ')
# print("bye")
#
#

##############


def introduceyourself(**info): #unknown number keyword arguments kwargs
    print(info)


introduceyourself(name='noha', work='iti', hoppy='reading', salary=1000)
introduceyourself()

introduceyourself(fname='toqa', lname='mohamed')


message = "thank you {stdname} for your help"
print(message.format(stdname='Rawan'))