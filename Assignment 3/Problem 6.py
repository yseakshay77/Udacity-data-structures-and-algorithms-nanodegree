def get_min_max(ints):

    if not ints:
        return
    arr = ints
    min = arr[0]
    max = arr[0]
    for a in arr:
        if a < min:
            min = a
        elif a > max:
            max = a
    return min ,max

#Test Cases
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)




print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")  # Pass
print("Pass" if ((0, 9) == get_min_max([0])) else "Fail")  # Fail
print("Pass" if ((0, 0) == get_min_max([0])) else "Fail")  # Pass
print("Pass" if (None is get_min_max([])) else "Fail")  # Pass


# Array with negative numbers
arr = [9,8,99,6,22,55,-30,-65,56]
print("Pass" if ((-65, 99) == get_min_max(arr)) else "Fail")  # Pass
