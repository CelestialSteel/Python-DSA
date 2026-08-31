
## program that asks a user the number of days and calculates the number of seconds in that number of days

days= int(input("Enter the number of days: "))
 ##typecasts the input to an integer

seconds = days * 86400
## calculates the number of seconds in the given number of days

print("The number of seconds in", days, "days is", seconds)
## PRINT STATEMENT