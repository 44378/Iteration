#Jack Scaife
#07/11/2014
#n! factorial return

import math

count = 0
total = 0
target = int(input("Please enter the number of which to end a positive factorial addition: "))

while count< target+1:
    total= total + count
    count=count+1

print("The sum of all the integers within this range is {0}.".format(total))

