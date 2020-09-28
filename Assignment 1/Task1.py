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

sending_number_texts = [row[0] for row in texts]
answering_number_texts = [row[1] for row in texts]
calling_number_calls = [row[0] for row in calls]
answering_number_calls = [row[1] for row in calls]

list_set1 = set(sending_number_texts)
unique_list1 = (list(list_set1))

list_set2 = set(answering_number_texts)
unique_list2 = (list(list_set2))

list_set3 = set(calling_number_calls)
unique_list3 = (list(list_set3))

list_set4 = set(answering_number_calls)
unique_list4 = (list(list_set4))

unique_list1.extend(unique_list2)
unique_list1.extend(unique_list3)
unique_list1.extend(unique_list4)

list_set = set(unique_list1)
unique_list = (list(list_set))

"""
Records from both texts and calls files are considered for finding unique numbers
"""

print("There are {} different telephone numbers in the records.".format(len(unique_list)))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."

complete
"""
