import  sys
def sort_012(input_list):

    a = input_list
    lo = 0
    hi = len(input_list) - 1
    mid = 0
    # f = [0] * 4
    input_freq = [0] * 10
    for num in input_list:
        input_freq[num] += 1

    # print (input_freq)
    # print (input_freq[3])

    for i  in  range(3,9):
        if input_freq[i] == 1:
            print (input_list)
            print("Only 0,1,2 values are allowed in array")
            sys.exit()

    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi - 1
    return a

def test_function(test_case):
    if not test_case:
        print ("Given list is Empty")
        # sys.exit()
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print(sorted_array)
        print("Pass")
    else:
        print("Fail")
    print()


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])  # Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])  # Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])  # Pass
test_function([2, 1, 0, 2])  # Pass
test_function([0, 0, 0])  # Pass

#  For Empty List
test_function([])

# For other numbers
test_function([0, 0, 3])  # Fail   Exit program execution



