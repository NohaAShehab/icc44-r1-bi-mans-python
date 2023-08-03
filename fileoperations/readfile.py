

"""
    1- open file
        --> decide mode
            read , write , append

    2- do operation
        read , write
         read mode ---> open file for reading starting from the beginning of the file

    3- close file

    module --> .py file (extension -> .py)

"""

""" openinig file  """
"""

        resourceobject=open(filename, filemode)
        this object will be used later in the file operations
"""


try:
    fileobject = open("myinfo.txt" , 'r')
except Exception as e:
    print(e)
    exit()
else:
    print(fileobject)
    # to read content
    data = fileobject.read()  # read file content into one string ?
    print(data)
    ## return the cursor to the beginning of the file
    fileobject.seek(0)

    data = fileobject.readlines()  # read file content into list --> each line is an element in the list
    print(data)

    fileobject.close()