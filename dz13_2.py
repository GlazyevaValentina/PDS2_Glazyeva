import random
from random_words import RandomWords
import time

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.random_words())

print("Original Int List:", int_list)
print("Original Float List:", float_list)
print("Original String List:", str_list)


# Bubble Sort Algorithm
def bubble_sort(data,numb_iter):
    length = len(data)
    counter_iter = []
    for n in range(1, numb_iter + 1):
        start = time.time()
        for iIndex in range(length):
            swapped = False
            for jIndex in range(0, length - iIndex - 1):
                if data[jIndex] > data[jIndex + 1]:
                    data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
                    swapped = True

            if not swapped:
                break
        end = time.time()
        requate_time = end - start
        counter_iter.append(requate_time)

    print("Bubble Sorting List: ", data)
    print(f"Average sorting time = {sum(counter_iter)/numb_iter}")


copy_my_list = int_list
bubble_sort(copy_my_list, 10)


copy_my_float_list = float_list
bubble_sort(copy_my_float_list, 10)

copy_my_str_list = str_list
bubble_sort(copy_my_str_list, 10)
