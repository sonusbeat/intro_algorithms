# Write a program takes an user input for an exam mark, and prints
# the grade for that mark - according to the following scheme:

#   Mark      Grade
#   >= 90       A
#  [80-90)      B
#  [70-80)      C
#  [60-70)      D
#    < 60       F
#
# The square and round brackets denote closed and open intervals(range).
# A closed interval includes the number, and open interval excludes it.
# Test your program by print the mark and the grade for a number of different marks.

exam_mark = int(input("Enter the exam mark: "))

if exam_mark >= 90:
    print("You get an A")
elif 80 <= exam_mark < 90:
    print("You get an B")
elif 70 <= exam_mark < 80:
    print("You get an C")
elif 60 <= exam_mark < 70:
    print("You get an D")
elif exam_mark < 60:
    print("You get an F")
