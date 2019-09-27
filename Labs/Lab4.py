""" Guessing Game """
import random


def guessing_game():
    answer = random.randint(1, 1000)  # generate a random integer from 1 to 1000
    # your code goes here.
    print(answer)
    pass


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game()



