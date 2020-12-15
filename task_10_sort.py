import random


def part(arr, min, max):
    piv = arr[min]
    i = min
    temp = 0
    temp_1 = 0
    for j in range(min+1, max+1):
        if arr[j] > piv:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i],arr[min] = arr[min],arr[i]
    return i


def quick_sort(arr, min, max):
    if min < max:
        pi = part(arr, min, max)

        quick_sort(arr, min, pi)
        quick_sort(arr, pi + 1, max)
    return arr


initial_numbers = list()

for i in range(0,50):
    initial_numbers.append(random.random())

print("Initial array of numbers:")
print(*initial_numbers, sep = "\n")

sorted_numbers = quick_sort(initial_numbers, 0, len(initial_numbers)-1)

print("\n\nSorted array of numbers:")
print(*sorted_numbers, sep= "\n")

initial_numbers.sort()

initial_numbers.reverse()

if initial_numbers == sorted_numbers:
    print("\n\nSorting algorithm works correctly!")

else:
    print(*initial_numbers, sep="\n")
    print("\n\nSorting algorithm does not work correctly!")





