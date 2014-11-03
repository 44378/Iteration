#Jack Scaife
#31/10/14
#Password exp



invalid = True
while invalid:
    password = input("Please enter the password: ")
    if password == "activate":
        invalid = False
    else:
        print("Re-enter correct password")

print("You entered {0}".format(password))
print("This is a valid")
