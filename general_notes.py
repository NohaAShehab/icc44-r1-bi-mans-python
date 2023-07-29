#
#
# l= [0,1,2,3,4]
# for i in l:
#     print("Hello world")

"target generate ranges of values"


myrange= range(5)  # iterable object

print(myrange, type(myrange))

# for num in myrange:
#     print(num)

for num in myrange:
    print(f"Hello world {num}")


# range object can be casted to a list ?
rr = list(myrange)


"customize range object ? "
# range(start, stop, step)
# rr = range(1,10, -1)
# print(list(rr))

#
# rr=range(10, 1, -1)
# print(list(rr))

#############################

# ll = ["ahmed", "ali","Mohamed", 'test', "iti"]
# print(ll[len(ll)-1])
# ## slicing
# print(ll[-1])
#
# print(ll[2:])
# print(ll[::-1])
#
# name= "noha"
# print(name[::-1])

###################
#  while loop with unknown number of iterations.
# while True:
#     age= input("please enter age ")
#     if age.isdigit():
#         print(age)
#         break
#
#     print("---- please enter valid age:  ")


# count = 0
#
# while count <5:
#     print("hello world")
#     count +=1

### continue , break with loops (for/ while loop)

# for item in range(10):
#     if item==4:
#         break  # break this loop
#
#     print(item)
#
# print("--- after the loop")

###
# for item in range(10):
#     if item == 4:
#         continue  # skip this iteration
#
#     print(item)
#
# print("--- after the loop")

################

# for count in range(3):
#     password =  input("please enter password")
#     if password=="123":
#         print("--- logged in successed ---")
#         break
#
#     print("-- invalid password , please try again")
#
# #### let loop ended successfully
# if count==2:
#     print("--- your account has been locked")


#
# for count in range(3):
#     password =  input("please enter password")
#     if password=="123":
#         print("--- logged in successed ---")
#         break
#
#     print("-- invalid password , please try again")
# else:
#     print("--- your account has been locked")
#
#



""" 

if(){}


"""
name=""
if name:
    pass

print("--- test")