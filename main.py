def askforInt():
    # when I call the function , ask user to enter number
    while True:
        num = input("please enter number : ")
        if num.isdigit():
            return  int(num)  # end the function
        print("--- please enter valid number ---")

askforInt()