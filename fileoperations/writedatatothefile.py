


"""


    open(filename, 'w')

    when you open file with w mode ---> if file doesn't exist
    the python tries to create it
    if file exists ---> open file for writing starting from
    the beginning of the file  ---> remove old content


"""

try:
    fileobject = open("mycv.txt","w")
except Exception as e:
    print(e)
else:
    print(fileobject)
    # fileobject.write("---- Hello world ----\n")
    # fileobject.write("---- bye----")
    fileobject.writelines(['ahmed', "ali", "mohamed"])
    fileobject.close()