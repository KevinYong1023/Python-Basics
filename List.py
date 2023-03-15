names = ["A", "E", "I", "O", "U"]
# Print out an item from the list
print(names[0])  # return "A"
print(names[1])  # return "E"
print(names[-2])  # return "O"
# Replace an item on the list
names[0] = "G"
print(names)
# Return a new list based on the specific range:
print(names[0:2])

numbers = [1, 2, 3, 4, 5]
print(len(numbers))
numbers.insert(5, 6)
print(numbers)
numbers.remove(5)
print(numbers)
numbers.clear()
print(numbers)
print(8 in numbers)

# Tuples:
values = (1, 2, 3)
print(values.count(3)) # count the inserted value in the Tuple list
print(values.index(1)) # return the value of the position
