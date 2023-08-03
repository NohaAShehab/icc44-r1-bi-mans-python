"""

Word guessing game (hangman)
○
A list of words will be hardcoded in your program, out of
which the interpreter will
○choose 1 random word.
○The user first must input their names
○
Ask the user to guess any alphabet. If the random word
contains that alphabet, it
○will be shown as the output(with correct placement)
○Else the program will ask you to guess another alphabet.
○Give 7 turns maximum to guess the complete word.


"""
""" iti"""


# name= 'test'
# name = enumerate(name)
# for index, char in name:
#     print(f"{index},{char}")
def get_locations_of_char(inputword, inputchar):
    indices = []
    for index, char in enumerate(inputword):
        if char == inputchar:
            indices.append(index)

    return indices


def hangman():
    words = {"iti", "python", "kiwi", "orange", "bi", "happy", "stressed"}
    playername = input("Please enter your name to start the game: ")
    selected_word = words.pop()
    user_trails = ["-"] * len(selected_word)
    """Guess a word consists of 4 chars ===> (----)"""
    print(f"""Welcome {playername}, You have only 7 trials
Try to guess a word like: {"".join(user_trails)} """, )

    for i in range(1, 8):
        inputchar = input(f"please enter your {i} Trial: ")
        if len(inputchar) == 1:
            selected_index = get_locations_of_char(selected_word, inputchar)
            for index in selected_index:
                user_trails[index] = inputchar
            print(''.join(user_trails))
            if user_trails == list(selected_word):
                print("==== You won Congratuations =====")
                break
        else:
            print("----- failed try")
    else:
        print("---- You failed -----------")


hangman()
