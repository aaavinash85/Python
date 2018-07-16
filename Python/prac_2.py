#Wap to ask the user to enter the name and age and display the year when the user becomes 100 year old name=raw_input('enter your name  ')
name =raw_input("What is your name: ")     # raw_input is used to get the string values
age = int(input("How old are you: "))      # input is used to get the interger and other values
year = str((2014 - age)+100)               # The str coerces data into a string.
print(name + " will be 100 yearsold in the year " + year)