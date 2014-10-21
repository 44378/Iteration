#Jack Scaife
#20/10/14
#Iteration Rev Ex Num.3

numbers_amount = int(input("Enter the amount of numbers to be averaged"))
total = int(0)

for count in range(numbers_amount):
    number_enter = int(input("Enter a number"))
    total=total+number_enter

average_num = total/numbers_amount

print("The average of these numbers is {0}".format(average_num))
