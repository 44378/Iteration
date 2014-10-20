#Jack Scaife
#20/10/14
# program to prompt for 8 numbers and report the total to the user
total=0
for count in range(1,9):
    num = int(input("Enter a number : "))
    total = total+num
print(total)
