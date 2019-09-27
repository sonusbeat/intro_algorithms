# Errors

# Syntax(grammar) Error: happens when Python cannot interpret your code,
# since we didn't follow the correct syntax for Python.
# These errors your're likely to get when you make a typo.

# msg = "Hello, World # Forget to close quotes

# Exceptions: happens when unexpected things happen during the execution
# of a program (run-time), even if the code is syntactically correct.
# There are different types of built-in exceptions in Python, and you can see
# which exception is 'thrown' in the error message.
# -> please "red the error message!"
# -> they are not supposed to scare you.
# -> they are trying to help you.
# (red underline) - (compile)

# try-except block
while True:
    try:
        a = int(input("Enter a first number: "))
        b = int(input("Enter a second number: "))
        c = a / b
        print(c)
        break
    except ValueError as error:
        print(f"Invalid inout: {error}")
        print("Invalid input. Please enter a number!")
    except ZeroDivisionError as error:
        print(f"Invalid input: {error}")
    except KeyboardInterrupt:
        print("\nNo input taken.\n")
        break
    except EOFError as error:
        print(f"{error}")
        break
    finally:
        print("Print Done!")

# Value Error
# n = int(input("Enter a number: "))

# KeyboardInterrupt : ^ + c
# EOF : ^ + d

# convertable = True
#
# for ch in n:
#     if ch.isdigit():
#         convertable = False
#     if convertable:
#         n = int(n)
#     else:
#         print("E")
