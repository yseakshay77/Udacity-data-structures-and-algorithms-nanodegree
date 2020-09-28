"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
print('reading text file is completed')
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
print('reading calls file is completed')

first_last_text = [ texts[0], calls[-1] ]
first_last_calls = [ calls[0], calls[-1] ]


result = [ texts[0], calls[-1]]
print("the first and last entry " + str(result))
print("First record of texts " + str(texts[0][0]) + " texts " +  str(texts[0][1])  + " at time " + str(texts[0][2]))
print("Last record of calls " + str(calls[-1][0]) + " answering number " +  str(calls[-1][1])  + " at time " + str(calls[-1][2]) + " lasting " + str(calls[-1][3]))

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
print("First record of texts " + str(texts[1][0]) + "texts" +  str(texts[1][1])  + " at time " + str(texts[1][2]))
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""