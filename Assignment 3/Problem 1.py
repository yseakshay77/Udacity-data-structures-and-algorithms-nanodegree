def sqrt(number):
    # print (number)
    flag = 0
    if number < 0:
        number =  abs(number)
        flag = 1

    low = 0
    high = number
    while low <= high :
        mid = (low + high) // 2
        mid_square = mid * mid
        if mid_square <= number :
            low = mid + 1
        else:
            high = mid -1

    if flag == 1:
        result = low-1
        return str(result) + "i"
    else:
        return  low-1

print ("Pass" if  (6 == sqrt(37)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

"""
For negative number 

* Negative numbers don't have real square roots since a square is either positive or 0
* for reference :-  https://www.expii.com/t/complex-square-roots-of-a-negative-real-number-4947 
* Here 6 is square root of 37 and for -37 it is 6i where i is imaginary part(Complex Number)
"""
print ("Pass" if  ("6i" == sqrt(-37)) else "Fail")
