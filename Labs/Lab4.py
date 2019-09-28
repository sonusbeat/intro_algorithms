""" Guessing Game """
import random

def guessing_game():
    answer = random.randint(1, 1000)
    while True:
        try:
            solved = False
            times = 0
            lower = 1
            higher = 1000
            print("Let's play a game!\nGuess a number between 1 and 1000")
            number = int(input())
            print("-" * 60)

            while not solved:
                if number == 0:
                    times += 1
                    print(f"You put 0, it's not allowed, try again!")
                    print(f"Attempts: {times}")
                    number = int(input())
                    print("-" * 60)

                if number > 1000:
                    times += 1
                    print(f"You put {number}, is greater than 1000, try again!")
                    print(f"Attempts: {times}")
                    number = int(input())
                    print("-" * 60)

                if number > answer < 1001:
                    times += 1

                    if higher > answer:
                        higher = number

                    print(f"Wrong, Your number should be from {lower} to {higher}, try again!")
                    print(f"Attempts: {times}")
                    number = int(input())
                    print("-" * 60)

                if number < answer:
                    times += 1

                    if lower < answer:
                        lower = number

                    print(f"Wrong, Your number should be from {lower} {higher}, try again!")
                    print(f"Attempts: {times}")
                    number = int(input())
                    print("-" * 60)

                if number == answer:
                    times += 1
                    solved = True
                    if times == 1:
                        print("Amazing you did it in 1 attempt")
                        print(f"You should play lottery today with the number {answer}")
                        break
                    else:
                        if times < 10:
                            print("You're a Gorgeous!")
                            print(f"It took!, {times} attempts")
                        elif times > 10 < 20:
                            print("Well Done!, You're in the average players!")
                            print(f"It took!, {times} attempts")
                        elif times > 20:
                            print("Well Done, You need more practice!")
                            print(f"It took!, {times} attempts")
                        break
            break
        except ValueError:
            print("Enter only digits!")
            break
        except KeyboardInterrupt:
            print("\nYou've logged out!")
            break
        finally:
            print(f"Game Over")


if __name__ == '__main__':
    guessing_game()

