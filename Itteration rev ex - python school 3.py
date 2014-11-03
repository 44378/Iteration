#Jack Scaife
#31/10/14
#Squaring from range

end = int(input("Please enter a number for which the leading numbers will be shown as well as their square: "))

count = 0

while count < end+1 :
    count_sq = count*count
    print("{0} squared is {1}".format(count,count_sq))
    count = count+1
    

