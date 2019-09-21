"""
Binary Search
- how you look up a word in a dictionary or a contact in phone book.
* Items have to be sorted!
"""

alist = [
    "Australia", "Brazil", "Canada", "Denmark",
    "Ecuador", "France", "Germany", "Honduras",
    "Iran", "Japan", "Korea", "Latvia",
    "Mexico", "Netherlands", "Oman", "Philippines",
    "Qatar", "Russia", "Spain", "Turkey",
    "Uruguay", "Vietnam", "Wales", "Xochimilco", "Yemen", "Zambia"
]

def binary_search(collection, target):
    start = 0
    end = len(collection) - 1
    steps = 0
    while start <= end:
        mid = (start + end) // 2
        steps += 1
        if collection[mid] == target:
            steps_message = "s" if steps > 1 else ""
            return F"\"{collection[mid]}\" is at position {str(mid)} and it took {str(steps)} step{steps_message}"
        elif collection[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return F"Your country \"{target}\" is not on the list!"


print(binary_search(alist, input("What's your country? ")))
