def rearrange_digits(input_list):
    input1 = input_list[0]
    x = 0

    _len = len(input_list[0])
    if _len <= 1:
        return [-1, -1]

    # ****** Sorting fun ***********************
    # Number = len(input1)
    # for i in range(len(input1)):
    #     for j in range(i + 1, Number):
    #         if (input1[i] < input1[j]):
    #             temp = input1[i]
    #             input1[i] = input1[j]
    #             input1[j] = temp
    #
    # # print(input1)
    # input = input1

    #  Heap Sort function
    def heapify(arr, n, i):
        # Find largest among root and children
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        # If root is not largest, swap with largest and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def heapSort(arr):
        n = len(arr)

        # Build max heap
        for i in range(n // 2, -1, -1):
            heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            # Swap
            arr[i], arr[0] = arr[0], arr[i]

            # Heapify root element
            heapify(arr, i, 0)
        return arr

    # Used to reverse sorted list
    def reverse(input2):
        i = 0  # first item
        j = len(input2) - 1  # last item
        while i < j:
            input2[i], input2[j] = input2[j], input2[i]
            i += 1
            j -= 1
        return input2

    input2 = heapSort(input1)
    input = reverse(input2)

    # input.sort()

    for i in range(0, len(input), 2):
        x = x * 10 + input[i]
    # print(x)
    y = 0
    for i in range(1, len(input), 2):
        y = y * 10 + input[i]
    return x, y


def test_function(test_case):
    output = rearrange_digits(test_case, )
    solution = test_case[1]
    # print(output)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 321]])  # fail
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]  #
test_function(test_case)  # Pass

test_function([[], [-1, -1]])  # pass
test_function([[0], [-1, -1]])  # pass
test_function([[0, 0], [0, 0]])  # Pass
test_function([[1, 1, 1, 3, 5, 6], [631, 511]])  # Pass
