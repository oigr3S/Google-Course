#!/usr/bin/env python3

#function to convert input hours, minutes to seconds
def to_seconds(hours, minutes, seconds):
    """This function converts user input (hours or minutes) into seconds"""
    return hours*3600+minutes*60+seconds

#print message to the user that the program has been initialised
print("The converter has been initialised")

#set the variabale paramenter for the while loop
cont= "y"
#if the user input is equal y (yes) the program will continue to run
while(cont.lower()) == "y":
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: "))

    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Would you like to do another conversion [y to continue] ")

print("Good bye!")
