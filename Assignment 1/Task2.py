"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

duration_calls = [row[3] for row in calls]

m = duration_calls[0]

for i in range(len(duration_calls)):        #calculating max Duration call
    if int(duration_calls[i]) > int(m):
        m=duration_calls[i]

print(m + " is Max Call Duration")

for i in range(len(calls)):
    if calls[i][3] == m:
        print( calls[i][1] + " spent the longest time, " +  m + " seconds, on the phone during September 2016.")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".

** for i in range(len(calls)):   at this line of code len(calls) gives int value which is no it iterable
    for i in range(len(calls)):   we used range() function to make "calls" iterable
"""

