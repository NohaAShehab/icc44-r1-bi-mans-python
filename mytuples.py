"""

    tuple 000> are immutable datatype
    you can access tuple items --> using index ?
    you cannot modify items after tuple creation

"""

# "1- define tuple"
t = ()
myt = tuple()
#
"2- tuple can hold different data from different data types"
myt = ("eman", "Ahmed", "Mohamed", 29, 10,5, True, "iti", "iti")
#
"""3- you can access element using index  --> start from zero"""
print(myt[4])
# print(myt[10])  #IndexError: tuple index out of range
#

"5- get len of tuple "
print(len(myt))
"6- count occurence of element in the tuple"
print(myt.count("iti"))
#
"7- you can loop over the tuple items"
for item in myt:
    print(f"item= {item}")

#
"8- check if element exists in the tuple"
print("iti" in myt)
#



""" 11- get index of element in the tuple """

print(myt.index("iti"))  # return with the index of the first occurrence of the element

# print(myl.index("noha")) #ValueError: 'noha' is not in tuple

"""12- concat the tuple """
courses = ("python", "sql", "xml", "power bi")
foundation_Courses= ("operating systems", "xml", "networks", "testing")

tuple_of_courses = courses + foundation_Courses
print(tuple_of_courses)


#
# """ 15- get min max tuple items ---> must be from the same type """
names=  ("Ahmed", "ali")
print(min(names))
#
"""16- print index of elements in the tuple """

# for name in names:
#     print(f"name= {names.index(name)}: {name}")
# index = 0
# for name in names:
#     print(f"name= {index}: {name}")
#     index +=1

"enumrate function ? ===? create index for the iterable "

enum_names= enumerate(names)  #
print(enum_names)  # <enumerate object at 0x7fc987722bc0>

for index, item in enumerate(names):
    print(f"index={index}, item = {item}")


#
#
"""17- cast string to a tuple """
#
name= "noha"
name= tuple(name)
print(name)
#
""" you can join tuple of strings to new string """
message= ("I", "am", "happy")
## "Seperator.join(iterable)
message=  "__".join(message)
print(message)


# """ empty tuples are falsy values """
tt= ()
if tt:
    print('hi')
else:
    print("bye")


# tuple of one item

courses = ('python',) # this a tuple of one item
print(courses, type(courses))


# you can cast tuple to a list and vise versa ?

workdays = ("Monday", "Wednesday")

workdays= list(workdays)
workdays.append("Sunday")
workdays= tuple(workdays)

#################################################################
## typle vs list ---> immutable --> hashing
# tuple hashable datatyopes

# hashing one way encryption
## all the primitive datatypes --> hashable ((immutable))



#####################################



myt = ("sat", "python", 12, 29 , ["hazem","Ahmed", "akram"],("room", "brainstormin") )
print(myt)

myt[4].append("Mohamed")
print(myt)
















