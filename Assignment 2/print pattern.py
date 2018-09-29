# ask for the max number of * in a row
maxLen = -1
try:
    maxLen = int(input("Please enter the max number of * star to be printed in a row: "))
except:
    print("Input is invalid, please try a valid number!!")
# everything is good if reached this point
# initialize an empty string
string = ""
# loop for for number of rows
for i in range(maxLen):
    
    # clear the string for every row
    string = ""
    
    # loop for column in i'th row (remember, i starts with 0, so increase it by 1)
    for j in range(i+1):

        # append * (i+1) times 
        string += "*"

    # print the upper half of the required pattern
    print(string)
# reset the string for reverse printing
string = ""

# since we've already printed the max number of * in the last line, 
# to print in reverse order we need to start the loop with (maxLen - 1) and decrement with -1
for i in range(maxLen - 1, 0, -1):

    # clear string for every row
    string = ""

    # loop for column in i'th row
    for j in range(i):

        # append * i times
        string += "*"

    # print the lower half of the pattern
    print(string)
