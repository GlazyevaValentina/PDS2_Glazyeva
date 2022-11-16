import sys

correct_unique_list = ['1', '2', '3', '4', '5', '6']
incorrect_list = ['1', '2', '3', '4', '5', '6', '5', 'word']
correct_non_unique_list = ['1', '2', '3', '4', '5', '6', '1', '2']


def unique(list):
    for index in range(len(list)):
        try:
            list[index] = int(list[index])
        except ValueError:
            print("\nList includs incorrect symbols. Try again")
            sys.exit()
    print("\nThere are no incorrect symbols in list")

    for i in list:
        if list.count(i) > 1:
            print("Not all elements in list are uniques")
            return False
    print("All elements in list are unique ")
    return True

unique(correct_unique_list)
unique(correct_non_unique_list)
unique(incorrect_list)