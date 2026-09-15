# Conditional Statements

x = 10
if x > 5:
    print("x is greater than 5")
    print("x is:", x)

## if-else statement
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

## if-elif-else statement
z = 7
if z > 10:
    print("z is greater than 10")
elif z > 5:
    print("z is greater than 5 but not greater than 10")
else:
    print("z is not greater than 5")

## Nested if statement
a = 15
if a > 10:
    if a > 20:
        print("a is greater than 20")
    else:
        print("a is greater than 10 but not greater than 20")
else:
    print("a is not greater than 10")

## Logical Operators
b = 8
if b > 5 and b < 10:
    print("b is greater than 5 and less than 10")
if b > 5 or b < 10:
    print("b is greater than 5 or less than 10")

### Ternary Operator
c = 12
result = "c is greater than 10" if c > 10 else "c is not greater than 10"
print(result)

# conditional expression
d = int(input("Enter a number: "))
result = "d is greater than 5" if d > 5 else "d is not greater than 5"
print(result)
