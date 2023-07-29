"""

    list 000> are mutable datatype
    you can access/modify list items --> using index ?

"""

"1- define list"
l = []
myl = list()

"2- list can hold different data from different data types"
myl = ["eman", "Ahmed", "Mohamed", 29, 10,5, True, "iti", "iti"]

"""3- you can access element using index  --> start from zero"""
print(myl[4])
# print(myl[10])  #IndexError: list index out of range

"""4- modify element in the list """
myl[4] = 'updated value'
print(myl)

# myl[10]="updated value" #IndexError: list assignment index out of range

"5- get len of list "
print(len(myl))
"6- count occurence of element in the list"
print(myl.count("iti"))

"7- you can loop over the list items"
for item in myl:
    print(f"item= {item}")


"8- check if element exists in the list"
print("iti" in myl)

"9- you can append elements to the list  --> add element at the end of the list"
myl.append("appended_element")

"-- can hold different types of data even anotherlist"
# myl.append(["python", "SQl", "xml"])  # append new element at index  --> 10
# print(myl[10][2])


"""insert element at certain position """
myl.insert(5, "inserted element")

myl.insert(100, "inserted element")  # if index doesn't exist --> add it to the end of the list

"""10 - remove element from the list """

"""pop element form the list """
# popped_element=myl.pop()  # return  with the last element of the list ?
# print(popped_element)
# print(myl)

popped_element=myl.pop(6)  # return  with the  element at the given index
print(popped_element)
print(myl)

""" remove element, unknown index """
myl.remove("iti")  # remove the first occurence of the element in the list
print(myl)

""" 11- get index of element in the list """

print(myl.index("iti"))  # return with the index of the first occurrence of the element

# print(myl.index("noha")) #ValueError: 'noha' is not in list

"""12- concat the list """
courses = ["python", "sql", "xml", "power bi"]
foundation_Courses= ["operating systems", "xml", "networks", "testing"]

list_of_courses = courses + foundation_Courses
print(list_of_courses)

"13- extend  a list "
courses.extend(foundation_Courses)  #extend courses list with content of the foundation list
print(courses)

"14- sorting list ---> items must be from the same type -// sorting based on comparison"

names = ["mohamed", "Islam", "Ahmed", "Ziad", "Ali", "Zaki", "Ayman", "ibrahim", "mohamed"]
print(names)
# names.sort() # sort the elements in the list ---> ascending
# print(names)
# names.sort(reverse=True) # sort the elements in the list ---> descending
# print(names)
### sorted(names)

""" 15- get min max list items ---> must be from the same type """
print(min(names))

"""16- print index of elements in the list """

# for name in names:
#     print(f"name= {names.index(name)}: {name}")
# index = 0
# for name in names:
#     print(f"name= {index}: {name}")
#     index +=1

"enumrate function ? ===? create index for the iterable "

# enum_names= enumerate(names)  #
# print(enum_names)  # <enumerate object at 0x7fc987722bc0>
#
for index, item in enumerate(names):
    print(f"index={index}, item = {item}")

#########33 format string --> f-format string
# name = input("please enter name: ")
# track = input("please enter track name: ")
# message = f"student name={name} studies at {track} track."  # format string based on existing variables
# print(message)


"""17- cast string to a list """

name= "noha"
name= list(name)
print(name)

""" you can join list of strings to new string """
message= ["I", "am", "happy"]
## "Seperator.join(iterable)
message=  "__".join(message)
print(message)

""" reverse list items """

myl = ['Ahmed', "iti", 2023, 29, 11,50, True, ["bi", "python"]]
myl.reverse()
print(myl)

""" empty lists are falsy values """
ll= []
if ll:
    print('hi')
else:
    print("bye")



