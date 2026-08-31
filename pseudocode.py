## program sets x to 0 and y to 20. Subsequently repeatedly subtracts 4 from y, add 2/y to x. THis happens until y is less than 6 then display x

x = 0
y = 20
while y > 6:
    y = y - 4
    x = x + 2/y
print(x)
