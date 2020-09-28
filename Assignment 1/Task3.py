"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

calling_numbers = [row[0] for row in calls]
called_numbers = [row[1] for row in calls]

Called_from_Bangalore = []

"""finding numbers called from banglore"""
for i in range(len(calling_numbers)):
    if calling_numbers[i].startswith('(080)'):
        Called_from_Bangalore.append(calls[i][1])

std_codes = []

"""Finding std numbers from the numbers calles from banglore"""
std_calls_from_banglore = [s for s in Called_from_Bangalore if "(0" in s]

"""Removing ()"""
for i in range(len(std_calls_from_banglore)):                                    #finding std codes and removing "()"  //complexity O(n)
    b=std_calls_from_banglore[i]
    std_codes.append(b[b.find("(")+1:b.find(")")])

""" Finding unique values"""
list_set = set(std_codes)
Final_std_codes = (list(list_set))

Final_std_codes.sort()

"""Finding mobile numbers called from Banglore"""
mobile_no_prefix = ['7','8','9']
mobile_numbers = []
mobile_numbers_codes = []
for i in range(len(Called_from_Bangalore)):
    if Called_from_Bangalore[i].startswith(tuple(mobile_no_prefix)):
        mobile_numbers.append(Called_from_Bangalore[i])
        mobile_numbers_codes.append(Called_from_Bangalore[i][0:4])

"""Finding Unique Mobile Prefixes"""
list_set1 = set(mobile_numbers_codes)
Final_mobile_prefixes = (list(list_set1))

Final_mobile_prefixes.sort()

print('The numbers called by people in Bangalore have codes: \n')
print(*Final_mobile_prefixes, sep = "\n")
print(*Final_std_codes, sep = "\n")

percentage_bang_calls = len(std_codes)/len(Called_from_Bangalore) *100
print("\n{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore: ".format(percentage_bang_calls))

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.


Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

>>> prefixes = ("a", "b", "c")
>>> targets = ["abar", "xbar"]
>>> filter(lambda t: t.startswith(prefixes), targets)

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""




