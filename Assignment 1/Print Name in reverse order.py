#Ask for name
name = input("Please enter your name:")
#split the name
splitStr = name.split()
#reverse it
splitStr.reverse()
#Print the output in reverse order
print("Your name is: ", " ".join(splitStr))
