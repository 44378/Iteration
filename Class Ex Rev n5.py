#Jack Scaife
#21/10/14
#Iteration Rev Ex Num.5

number = 0
total = 0
count = 0

while number >=0:
    number = int(input("Please enter a number to add to the average: "))

    if number>=0:
        total = total+number
        count = count+1
        
average = total/count
print("The average is:{0}".format(average))
