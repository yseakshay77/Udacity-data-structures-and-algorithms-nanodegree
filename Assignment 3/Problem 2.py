def Search(arr, key):
    n = len(arr)
    pivot = pivotFind(arr, 0, n - 1);

    if pivot == -1:
        return binarySearch(arr, 0, n - 1, key);
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binarySearch(arr, 0, pivot - 1, key);
    return binarySearch(arr, pivot + 1, n - 1, key);


def pivotFind(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low

        # low + (high - low)/2;
    mid = int((low + high) / 2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid - 1)
    if arr[low] >= arr[mid]:
        return pivotFind(arr, low, mid - 1)
    return pivotFind(arr, mid + 1, high)


def binarySearch(arr, low, high, key):
    if high < low:
        return -1

    # low + (high - low)/2;
    mid = int((low + high) / 2)

    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), high,
                            key);
    return binarySearch(arr, low, (mid - 1), key);



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    # print(type(input_list))
    number = test_case[1]
    re = Search(input_list, number)
    ree = linear_search(input_list, number)
    if re == ree :
        if re != -1:
            print("Pass")
        else:
            print("Given number not found")
    else:
        print("Fail")

# arr1 = [6, 7, 8, 9, 10, 1, 2, 3, 4]
# arr2 = [6, 7, 8, 1, 2, 3, 4]

test_function([[6, 7, 8,  9, 10, 1, 2, 3, 4], 100])  # Given number not found
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])    #Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])           #Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])           #Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])           #Pass

# Edge Cases
test_function([[], -1])                             # Given number not found
test_function([[1], 0])                             # Given number not found
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 22])   # Given number not found
