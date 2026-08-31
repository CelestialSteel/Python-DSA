## program takes 5 inputs from the user and calculates the average of those inputs entered into an array
## the array is then displayed followed by the average

array = []
## initializes an empty array
for i in range(5):
    array.append(float(input("Enter a number: ")))
    ## asks the user to input a number and appends it to the array using loops

average = sum(array) / len(array)
print(array)
print("The average of the numbers is", average) 