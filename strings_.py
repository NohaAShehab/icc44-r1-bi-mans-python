
"""
    string is primitive immutable datatype ---
    treated like an array

"""
""" define a string """
# name = "Islam"

"""get len of the string ? """
# print(len(name))

"2- access string parts using index start form 0"
# print(name[4])

""" 3- loop over the string """
# for char in name:
#     print(char)

""" operations on string (immutable)"""
""" styling of string """
# message = 'i love iti'
# upperstring= message.upper()
# message= message.upper()
#
#
# print(message.upper())  # return new string
# print(message.lower())  # return new string
# print(message.capitalize())  # return new string
# print(message.title())  # return new string
# print(message)
# print(upperstring)


""" check value inside the string """
# name = 'nagar '
# print(name.isupper())
# print(name.lower())
# print(name.isalpha())  # retrun --> A, z
# name="          "
# print(name.isspace())
# this string consists of spaces only--> True
name = "AbdAllah Ibrahim"
print(name.isspace())
#
# num = "iti"
# # num = int(num)
# if num.isdigit():
#     print("-----can be converted ")
#     num= int(num)
#     print(num, type(num))
# else:
#     print("--- cannot be converted ")

### accept input from user


# age = input("please enter age: ")  # return always with string
# print(age, type(age))
# t = type(age)
# print(type(t))  # object from class Type


### count accourence of char
# iti = "information tech institute"
# print(iti.count("i"))

## string formatting

""" concatentation """
fname = 'noha '
midname = 'abdelhady '
lname ='shehab '

# """contact string using + opertor """
#
# fullname = fname + midname + midname +lname
# print(fullname)
#
# "string interpolation"
#
# fullname = fname + midname*2 + lname
# print(fullname)

""" format string """
no_of_students = 25
track = "BI"
branch = "Mansoura"
# message = "we have " + str(no_of_students) + \
#           "in " +track +" track at" + branch
#
# print(message)


# temp = "we have {0} students in {1} track at {2} branch"
# print(temp.format(no_of_students, track, branch)) # return new string
# print(temp.format(track,no_of_students, branch))


""" keyword arguments format """


# temp = "we have {students} students in {trackname} " \
#        "track at {branchname} branch"
# print(temp.format(students=no_of_students,branchname=branch,
#                   trackname=track))
#

""" f-format string ---> based on existing varables"""

# temp = f"we have {no_of_students} students in {track} " \
#        f"track at {branch} branch {location} "
#
# print(temp)

""" replace part of string --> str with str ---> new string """


# message=  "we love iti i i i"
# print(message.replace("i", "$", 2))


"""strip function """

fullname ='  My name is noha   '
print(len(fullname))
##default behaviour strip white spaces from the begining and
# and the end of string
# print(fullname.strip(),len(fullname.strip()))

# print(fullname.lstrip(),len(fullname.lstrip()))
#

# strip specific char or set of char
sal = "    50000$"
sal = sal.strip("$ ")  #
print(sal)


message = "   I hope we can earn 100000 per month   $$  "
print(message.strip(" $"))






















































































