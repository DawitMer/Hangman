import random
word_list = ["aardvark", "baboon", "camel"]

hangman = [
    # Index 0: fully drawn
    r'''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    ''',

    # Index 1
    r'''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    ''',

    # Index 2
    r'''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    ''',

    # Index 3
    r'''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    ''',

    # Index 4
    r'''
    +---+
    |   |
    O   |
    |   |
        |
        |
    ''',

    # Index 5
    r'''
    +---+
    |   |
    O   |
        |
        |
        |
    ''',

]

word = random.choice(word_list)
print(word)

word_len = len(word)

#take time use other than for loop
# for i in range(0, word_len):
#     print("_", end="")
# print()
display = "_" * word_len
check = False
print(display)

live = 5
while live != -1 and display != word:
    check = False
    displaylist = list(display)
    Guess_letter = input("guess a letter").lower()
    for i in range(0, word_len):
        if word[i] == Guess_letter:
            displaylist[i] = Guess_letter
            check = True

    if not check:
        print(hangman[live])
        live -= 1

    display = ''.join(displaylist)
    print(display)

if live != -1:
    print("congratulations you have found the answer")
else:
    print("Game Over")