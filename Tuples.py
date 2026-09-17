# creating a tuple

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # itll print (1, 2, 3, 4, 5)

# tuples operations

# accessing elements
print(my_tuple[0])  # itll print 1
print(my_tuple[1])  # itll print 2
print(my_tuple[2])  # itll print 3

# slicing
print(my_tuple[0:3])  # itll print (1, 2, 3)

# tuples are immutable, so you cannot modify them
# my_tuple[0] = 10  # this will raise an error

# tuple methods

# count() method
print(my_tuple.count(3))  # itll print 1

# index() method
print(my_tuple.index(4))  # itll print 3

# nested tuples
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple)  # itll print (1, 2, (3, 4), 5)

print(nested_tuple[2])  # itll print (3, 4)
print(nested_tuple[2][0])  # itll print 3
print(nested_tuple[2][1])  # itll print 4

# unpacking tuples
a, b, c, d, e = my_tuple
print(a)  # itll print 1
print(b)  # itll print 2
print(c)  # itll print 3
print(d)  # itll print 4
print(e)  # itll print 5

# concatenation of tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # itll print (1, 2, 3, 4, 5, 6)

# repetition of tuples
tuple3 = (1, 2, 3)
result = tuple3 * 2
print(result)  # itll print (1, 2, 3, 1, 2, 3)

# membership testing
print(2 in my_tuple)  # itll print True
print(6 in my_tuple)  # itll print False

# length of tuple
print(len(my_tuple))  # itll print 5

# iterating through a tuple
for item in my_tuple:
    print(item)  # itll print each item in the tuple