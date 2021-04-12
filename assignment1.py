# Course: CS261 - Data Structures
# Student Name: Mason Stiller
# Assignment: Python Review
# Description: A collection of "totally code" of various functions having to do with Static Arrays
#that times out the auto grader

import random
import string
from a1_include import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> ():
    """
    Returns tuple of min and max within array
    """
    length = arr.size()
    max = 0
    min = 0
    i = 0

    while i < length:
        new = arr[i]
        i += 1
        if max == 0:
            max = new
        elif new > max:
            max = new
        if min == 0:
            min = new
        elif new < min:
            min =new

    return (min, max)
    pass


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Returns array with fizz, buzz, or fizzbuzz interject depend on if value is factor of 3, 5, or both 3 and 5
    """
    length = arr.size()
    copy = StaticArray(length)
    for i in range (0, length -1):
        copy[i] = 0
    index = 0

    while index < length:
        if arr[index] % 3 == 0:
            if arr[index] % 5 == 0:
                copy[index] = 'fizzbuzz'
                index += 1
            else:
                copy[index] = 'fizz'
                index +=1
        elif arr[index] % 5 == 0:
            copy[index] = 'buzz'
            index += 1
        else:
            copy[index]= arr[index]
            index += 1

    return copy
    pass


# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """
    Reverses the array
    """
    x = 0
    y = arr.size() -1
    while x <y:
        arr[x],arr[y] = arr[y], arr[x]
        x += 1
        y -= 1

    return arr
    pass


# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Rotates the array in the desired direction
    """
    length = arr.size()
    copy = StaticArray(length)
    for i in range (0, length):
        copy[i] = arr[i]

    if steps > 0:
        for i in range(0, steps):
            temp = copy[length - 1]
            for p in range(length - 1, 0, -1):
                copy[p] = copy[p - 1]
            copy[0] = temp

    elif steps < 0:
        for i in range(0, abs(steps)):
            temp = copy[0]
            for p in range (length -1):
                copy[p] = copy[p + 1]
            copy[length -1] = temp

    else:
        return copy

    return copy

    pass


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """
    Creates an Arrray with values in the desired range
    """
    output = StaticArray(abs(start-end) +1)
    last_index= output.size() -1
    if last_index ==0:
        output[0] = start
        return output
    else:
        output[0] = start
        output[last_index] = end
        if start < end:
            current = start
            for i in range(1, last_index):
                current += 1
                output[i] = current

            return output
        elif start > end:
            current = start
            for i in range(1, last_index):
                current -= 1
                output[i] = current
            return output
    pass


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """
    Determines if an array is sorted in ascending or descending order.
    """
    final_index = arr.size() -1
    if final_index == 0:
        return 1
    else:
        if arr[0] > arr[1]:
            for i in range (1, final_index -1):
                if arr[i] <= arr [i +1]:
                    return 0
            return 2


        if arr[0] < arr[1]:
            for i in range(1, final_index - 1):
                if arr[i] >= arr[i + 1]:
                    return 0
            return 1

    pass


# ------------------- PROBLEM 7 - SA_SORT -----------------------------------


def sa_sort(arr: StaticArray) -> None:
    """
    Sorts the array with the insertion sort method
    """
    length = arr.size()
    for i in range(1, length):

        val = arr[i]
        pos = i - 1
        while pos >= 0 and val < arr[pos]:
            arr[pos + 1] = arr[pos]
            pos -= 1
        arr[pos + 1] = val
    pass


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    removes duplicates from the array
    """
    length = arr.size()
    list= []
    list.append(arr[0])
    for i in range(0, length - 1):
        if arr[i + 1] != arr[i]:
            list.append(arr[i+1])

    output = StaticArray(len(list))
    for i in range(0, len(list)):
        output[i] = list[i]
    return output

    pass


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    sorts an array using the count sort method
    """
    length = arr.size()
    max = 0
    min = 0
    output = StaticArray(length)
    for i in range(0, length):
        output[i] = arr[i]

    i = 0


    while i < length:
        new = arr[i]
        i += 1
        if max == 0:
            max = new
        elif new > max:
            max = new
        if min == 0:
            min = new
        elif new < min:
            min = new

    count = [0] *((max - min) + 1)


    for i in range(0, length):
        if arr[i] <= max:
            j = (max - arr[i])
            count[j] += 1

    for i in range(1,len(count)):
        count[i] += count[i-1]

    for i in range(length):
        output[count[max - arr[i]] -1] = arr[i]

    return output

    pass


# ------------------- PROBLEM 10 - SA_INTERSECTION --------------------------


def sa_intersection(arr1: StaticArray, arr2: StaticArray, arr3: StaticArray) \
        -> StaticArray:
    """
    very badly determines if there are intersects within 3 different arrays
    """
    intersects = 0
    current = 0
    for i in range(0, arr1.size()):
        for j in range(current, arr2.size()):
            if arr1[i] == arr2[j]:
                intersects += 1
                current += 1

    interpair= StaticArray(intersects)
    for i in range(0, intersects):
        interpair[i] = 0

    current = 0

    for i in range(0, arr1.size()):
        for j in range(current, arr2.size()):
            if arr1[i] == arr2[j]:
                interpair[current] = arr1[i]
                current += 1

    interpairb= StaticArray(interpair.size())
    for i in range(0, interpair.size()):
        interpairb[i] = interpair[i]

    current = 0
    intersects = 0

    for i in range(0, interpairb.size()):
        for j in range(current, arr3.size()):
            if interpairb[i] == arr3[j]:
                interpairb[i] = None
                intersects += 1
                current += 1

    if intersects == 0:
        output = StaticArray(1)
        output[i] = None
    else:
        output = StaticArray(intersects)
        for i in range(0, intersects):
            output[i] = 0

    current = 0

    for i in range(0, interpair.size()):
        for j in range(current, arr3.size()):
            if interpair[i] == arr3[j]:
                output[current] = interpair[i]
                interpair[i] = None
                current += 1

    return output
    pass


# ------------------- PROBLEM 11 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Returns a sorted array of the squares of the input array.
    """
    length = arr.size()
    output = StaticArray(length)
    for i in range(0, length):
        output[i] = 0

    max = length-1
    p1 = length -1
    p2 = 0
    start = arr[p2]
    end = arr[p1]
    i = 0

    while p2 < p1:
        if abs(start) >= abs(end):
            output[max] = start**2
            max -=1
            p2+=1
            start = arr[p2]
        elif abs(start) < abs(end):
            output[max] = end ** 2
            max -= 1
            p1 -= 1
            end = arr[p1]
        i += 1

    return output
    pass


# ------------------- PROBLEM 12 - ADD_NUMBERS ------------------------------


def add_numbers(arr1: StaticArray, arr2: StaticArray) -> StaticArray:
    """
    Adds numbers in different arrays together into a new array
    """
    if arr1.size() >= arr2.size():
        start = arr1.size() -1
        output =StaticArray(arr1.size()+1)
        output[0] = 0
        index = output.size() - 1
        for i in range (arr2.size()- 1 , -1, -1):
            output[index] = arr2[i] + arr1[start]
            start -= 1
            index -= 1
        for i in range(output.size()):
            if output[i] == None:
                output[i] = arr1[i -1]
    else:
        start = arr2.size() -1
        output =StaticArray(arr2.size()+1)
        output[0] = 0
        index = output.size() - 1
        for i in range (arr1.size()- 1 , -1, -1):
            output[index] = arr1[i] + arr2[start]
            start -= 1
            index -= 1
        for i in range(output.size()):
            if output[i] == None:
                output[i] = arr2[i -1]

    index = output.size() - 1
    for i in range(index, 0, -1):
        if output[i] > 9:
            output[i] -= 10
            output[i -1] += 1

    if output[0] != 0:
        return output
    else:
        output_2 = StaticArray(index)
        for i in range(0, index):
            output_2[i] = output[i+1]
        return output_2
    pass


# ------------------- PROBLEM 13 - BALANCED_STRINGS -------------------------


def balanced_strings(s: str) -> StaticArray:
    """
    Cretaes the max amount of balanced strings into a static array
    """
    a_count= 0
    b_count = 0
    c_count = 0
    string_score = 0

    analyze = StaticArray(len(s))
    i = 0
    for char in s:
        analyze[i] = char
        i += 1
    splits = StaticArray(len(s))

    index = 0
    for i in range(analyze.size()):
        if analyze[i].lower() == 'a' :
           a_count += 1
           if a_count == b_count == c_count:
               string_score += 1
               splits[index] = a_count + b_count + c_count
               a_count = 0
               b_count = 0
               c_count = 0
               index += 1
        if analyze[i].lower() == 'b':
           b_count += 1
           if a_count == b_count == c_count:
               string_score += 1
               splits[index] = a_count + b_count + c_count
               a_count = 0
               b_count = 0
               c_count = 0
               index += 1
        if analyze[i].lower() == 'c':
            c_count += 1
            if a_count == b_count == c_count:
                string_score += 1
                splits[index] = a_count + b_count + c_count
                a_count = 0
                b_count = 0
                c_count = 0
                index += 1

    output = StaticArray(string_score)
    i = 0
    index = 0

    for j in range(splits.size()):
        newstring = ''

        if splits[j] == None:
            return output
        else:
            for p in range(0, splits[j]):
                newstring += str(analyze[index])
                index += 1
            output[i] = newstring
            i +=1
    pass


# ------------------- PROBLEM 14 - TRANSFORM_STRING -------------------------


def transform_string(source: str, s1: str, s2: str) -> str:
    """
    Converts a string to a new string with different characters
    """
    charsource =[]
    char_1 = []
    char_2 = []
    output = []
    outputstring = ""

    for char in source:
        charsource.append(char)
        output.append(None)
    for char in s1:
        char_1.append(char)
    for char in s2:
        char_2.append(char)

    for i in range(len(charsource)):
        if charsource[i].isalpha() == True:
            for p in range(len(char_1)):
                if charsource[i] == char_1[p]:
                    output[i] = char_2[p]
            if charsource[i].isupper() == True:
                if output[i] == None:
                    output[i] = ' '
            elif charsource[i].islower() == True:
                output[i] = '#'
        elif charsource[i].isdigit() == True:
            for p in range(len(char_1)):
                if charsource[i] == char_1[p]:
                    output[i] = char_2[p]
                elif charsource[i] != char_1[p]:
                    if output[i] == None:
                        output[i] = '!'
        else:
            output[i] = '='

    for char in output:
        outputstring += char

    return outputstring
    pass







# BASIC TESTING
if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))


    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))


    print('\n# min_max example 3')
    arr = StaticArray(3)
    for i, value in enumerate([3, 3, 3]):
        arr[i] = value
    print(min_max(arr))


    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)


    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)


    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        print(rotate(arr, steps), steps)
    print(arr)


    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))


    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)


    print('\n# sa_sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)],
        [random.randrange(-30000, 30000) for _ in range(5_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        sa_sort(arr)
        print(arr if len(case) < 50 else 'Finished sorting large array')



    print('\n# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)


    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [random.randrange(-499, 499) for _ in range(1_000_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = count_sort(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')


    print('\n# sa_intersection example 1')
    test_cases = (
        ([1, 2, 3], [3, 4, 5], [2, 3, 4]),
        ([1, 2], [2, 4], [3, 4]),
        ([1, 1, 2, 2, 5, 75], [1, 2, 2, 12, 75, 90], [-5, 2, 2, 2, 20, 75, 95])
    )
    for case in test_cases:
        arr = []
        for i, lst in enumerate(case):
            arr.append(StaticArray(len(lst)))
            for j, value in enumerate(sorted(lst)):
                arr[i][j] = value
        print(sa_intersection(arr[0], arr[1], arr[2]))


    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
        [random.randrange(-10_000, 10_000) for _ in range(1_000_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = sorted_squares(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')


    print('\n# add_numbers example 1')
    test_cases = (
        ([1, 2, 3], [4, 5, 6]),
        ([0], [2, 5]),
        ([2, 0, 9, 0, 7], [1, 0, 8]),
        ([9, 9, 9], [9, 9, 9, 9])
    )
    for num1, num2 in test_cases:
        n1 = StaticArray(len(num1))
        n2 = StaticArray(len(num2))
        for i, value in enumerate(num1):
            n1[i] = value
        for i, value in enumerate(num2):
            n2[i] = value
        print('Original nums:', n1, n2)
        print('Sum: ', add_numbers(n1, n2))


    print('\n# balanced_strings example 1')
    test_cases = (
        'aaabbbccc', 'abcabcabc', 'babcCACBCaaB', 'aBcCbA', 'aBc',
        'aBcaCbbAcbCacAbcBa', 'aCBBCAbAAcCAcbCBBa', 'bACcACbbACBa',
        'CBACcbcabcAaABb'
    )
    for case in test_cases:
        print(balanced_strings(case))


    print('\n# transform_strings example 1')
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
                  'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
                  'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
                  'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
                  'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
                  'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
                  'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
                  'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
                  'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
                  'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
                  'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')
    for case in test_cases:
        print(transform_string(case, '612HZ', '261TO'))
