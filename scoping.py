""" lexical scoping """

""" 1- how can we interact with variables defined inside the function
and how can the function interact with variables define in the script """
##
"""
  variable defined anywhere in the script  ---> variable with global scope   
  variable can be accessed anywhere anyscript 
"""


"""  ------------------------------ 
    variable defined in the script --> you read / print from inside a function

"""
"1- print course name from inside the function "

# course = 'python'  # global scope ?
#
# def printinfo():
#     name = input("please enter name: ")
#     print(name)
#     print(f"Course = {course} ---> from inside the function ")

# printinfo()

# def sayhi():
#     print(f"course = {course} --> from inside sayhi")
#
# sayhi()
#


"""variable defined inside the function  
has local scope ---> 
can be accessed only inside the function 

"""

# def askforstudent():
#     name = input("please enter name: ") # variable with localscope
#     print(f"from inside the function name= {name}")
#
# askforstudent()
# print("---------------")
# print(name)

"""modify global variable from inside a function """
# course= 'python'
# def modifycourse():
#     course = input("please enter course: ") # this new local variable
#     print(f"course=  {course} --> from inside the function ")
#
# modifycourse()
# print(f"course={course} ")  #still we have a problem


# course= 'python'
# def modifycourse():
#     global course
#     course = input("please enter course: ") # this new local variable
#     print(f"course=  {course} --> from inside the function ")
#
# modifycourse()
# print(f"course={course} ")  #still we have a problem

#
#
#
#
# no_of_visits= 0
# def openwebsite():
#     global  no_of_visits
#     print("--- welcome to out website", end=' ')
#     no_of_visits +=1
#     print(no_of_visits)
#
# openwebsite()
# openwebsite()
# openwebsite()
# openwebsite()
# openwebsite()
#
#


"""function inside a function """

#
# def askforname():
#     fname =input("please enter firstname")
#     lname= input("please enter lastname")
#
#     fullname = f"{fname} {lname}"
#     print(fullname)
#
#     def printformattedname():  # inner function
#         print(fullname.title())  # can access local variables in the parent function
#
#     printformattedname()
#
#
# askforname()


"""modify local variable from inside the inner function """

# def askforname():
#     fname =input("please enter firstname")
#     lname= input("please enter lastname")
#     fullname = f"{fname} {lname}"
#     print(fullname)
#
#     def modifyfull():  # inner function
#         fullname = "updated"  # create new local variable for the inner function
#         print(f"from inner {fullname}")
#
#     modifyfull()
#     print(f"from outer {fullname}")
#
# askforname()
# print("-------------")
#
#

"""====? """



def askforname():
    fname =input("please enter firstname")
    lname= input("please enter lastname")
    fullname = f"{fname} {lname}"
    print(fullname)

    def modifyfull():  # inner function
        nonlocal fullname  # please don't create new local variable use the local of the parent fun
        fullname = "updated"
        print(f"from inner {fullname}")

    modifyfull()
    print(f"from outer {fullname}")

# askforname()
# print("-------------")

###################


grade = 10

# def myfun():
#     print("---- my fun")
#     def modifygrade():
#         global  grade
#         grade = 100
#
#     modifygrade()
# myfun()
# print(grade)



def myfun():
    def outer1():
        course = 'py'
        def outer2():
            def outer3():
                nonlocal  course
                course = 'python'
            outer3()
        outer2()
        # print(course)
    outer1()

myfun()








# abdulrahman
# abdu
# lr
# ahm
# an
#
# noha
# no
# h
# a

"""
noha
[apple, iti, test]
hi noha 
-----

1:try --> m -->wrong
2:try ---> e  

____e

3: p
_pp_e



"""










