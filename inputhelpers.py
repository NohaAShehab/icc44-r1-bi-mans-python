happy = True

def askforInt(customized_message='please enter number'):
    # when I call the function , ask user to enter number
    while True:
        num = input(customized_message)
        if num.isdigit():
            return  int(num)  # end the function
        print("--- please enter valid number ---")

