

"""
Syntax error ---> must be resolved

logical error  --->


runtime error
"""

# def sumnum(num1, num2):
#     res= num1 * num2
#     print(res)
#
#
# sumnum(2,2)
# sumnum(4,5)


"""
    runtime error --> exceptions 
    interrupting execution 
"""
# unit tests for our scripts

# i=0
#
# while i < 5:
#     print(i)
#
#
#

""" runtime error"""
# print("---- hello world ----")
# print(name)


############
"""
    exception  --->unexpected error caused the application to stop 
    
    
"""
# from inputhelpers import  askforInt
# def divnums():
#     num1 = askforInt("please enter num1: ")
#     num2 = askforInt("please enter num2: ")
#     res = num1/ num2
#     print(res)

# divnums()



# num= int(input("please enter number "))
# print(num)


""" 
any runtime error must be handled 

"""


# num=int(input("please enter num: "))
# if num.isdigit():
#     print("--- tis a number ")  # AttributeError



# print(test)
#
# import os
# os.mkdir("test")


"""---------------  Exception handling -----------------"""
print("------- exception handling ----")
# try:
#     print(name)
# except:
#     print("---- variable not found ")
# print("---------- all is well -------")

# print(name)
# print("==== alll is well --------")
#
# def askforInt(message):
#     while True:
#         num = input(message)
#         try:
#             num= int(num)
#             return num
#         except:
#             print("--- please enter valid number ")
#
# age = askforInt("plz enter age: ")
# print(age)

##############################################################
#
# try:
#     num = int(input('please enter num'))
#     print(num)
#     print(name)
#     pass
#
# except Exception as myexception:
#     print(myexception)
#
#
# print("---- after the exception  -----")




#################################################

# try:
#     num1 = int(input("please enter num1 : "))
#     num2 = int(input("please enter num1 : "))
#     res = num1/ num2
# except ValueError as ve:
#     print(f"issue for the input values :  {ve}")
# except ZeroDivisionError as ze:
#     print(f"---- you cannot divide number by zero : {ze}")
#     print("---  the application will exit now ,"
#           " please recall the application with valid numbers ")
#     exit()
# except Exception as e:
#     print("---------- Ma3elsh--------")




#############################3

# try:
#     num1 = int(input("please enter num1 : "))
#     num2 = int(input("please enter num1 : "))
#     res = num1/ num2
# except ValueError as ve:
#     pass
# except ZeroDivisionError as ze:
#     pass
# except Exception as e:
#     pass
#
# print("----------------- Program exectuted successfully -----------")
#
# print(res)
#
#





# try:
#     num1 = int(input("please enter num1 : "))
#     num2 = int(input("please enter num1 : "))
#     res = num1/ num2
# except Exception as e:
#     print(f"---{e} ")
# else:
#     "this block will be exectuted only if there is no problem"
#     print(res)
#
# print("----------------- Program exectuted successfully -----------")




try:
    num1 = int(input("please enter num1 : "))
    num2 = int(input("please enter num1 : "))
    res = num1/ num2
except Exception as e:
    print(f"---{e} ")
else:
    "this block will be exectuted only if there is no problem"
    print(res)
finally:
    "mark that danger has passed "
    "this block will be executed always "
    print("----- Nawrtna ya fandem ----- ")

print("--------fdsdfjksdjkfn")
print("----------------- Program exectuted successfully -----------")