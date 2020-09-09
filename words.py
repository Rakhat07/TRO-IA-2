from random import choice


def change_turn(turn, name1, name2):
    if turn == name1:
        return name2
    else:
        return name1


def whose_turn(name1, name2):
    print("Who wants to be first?")
    print("")
    k = input(f"{name1} or {name2}?")
    if k == name1:
        return name1
    elif k == name2:
        return name2
    else:
        print("There is no name like this")


def random_words():
    words = {"sugar": "Clean, but not water,"
                 "White, but not snow,"
                 "Sweet, but not ice-cream,"
                 "What is it?",
             "fire": "I am always hungry,"
                     "I must always be fed,"
                     "The finger I touch,"
                     "Will soon turn red",}
    word = choice(["sugar", "fire"])
    znachenie = words[word]
    return word,znachenie


def main():
    name1 = input("first players name:")
    name2 = input("second players name:")
    turn = whose_turn(name1, name2)
    word, znachenie = random_words()
    word_list = list(word)
    game_over = False
    board = list("*" * len(word))
    points1, points2 = 0, 0
    dict = {name1: points1, name2: points2}
    print(dict)
    while not game_over:
        print("")
        print("------------------------------")
        print(f"{turn} points: {dict[turn]}")
        print(f"Guess a word: {' '.join(board)}")
        print(f"Hint: {znachenie}")
        user_guess = input("Enter a word or a letter: ")
        user_guess = user_guess.lower()
        if len(user_guess) == 1:
            if user_guess in board:
                print("this letter already guessed")
                dict[turn] -= 2
                turn = change_turn(turn, name1, name2)

            for i in range(len(word)):
                if word[i] == user_guess:
                    board[i] = user_guess
                    dict[turn] += 2
                    break
            if user_guess not in word_list:
                print("Thats incorrect")
                dict[turn] -= 2
                turn = change_turn(turn, name1, name2)

        else:
            if user_guess == word:
                print(f"Correct! Congratulations {turn}!")
                print(f"{name1} have:{dict[name1]} points")
                print(f"{name2} have:{dict[name2]} points")
                game_over = True


            else:
                print("Incorrect, think again.")
                turn = change_turn(turn, name1, name2)


main()