


"""


    open(filename, 'a')

    when you open file with a mode ---> if file doesn't exist
    the python tries to create it
    if file exists ---> open file for writing starting from
    the end of the file  ---> keep old content


"""

try:
    fileobject = open("mycv.txt","a")
except Exception as e:
    print(e)
else:
    print(fileobject)
    fileobject.write("---- Hello world ----\n")
    fileobject.write("---- bye----")
    fileobject.writelines(['ahmed', "ali", "mohamed"])
    fileobject.close()