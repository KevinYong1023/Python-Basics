# While loop
i = 0
while i <= 8:
    print(i)
    i = i + 1

i = 0
while i <= 8:
    print(i * "q")
    i = i + 1

# For Loop
numbers = ["a", "e", "i", "o", "u"]
for i in numbers:
    print(i)

# Range
# Print a range of 5 numbers
values = range(5)
for i in values:
    print(i)
# Print a range of 5 numbers until number 10
values1 = range(5,11)
for v in values1:
    print(v)
# Print a range of numbers from 2 to 10 and skip 3 numbers
values2 = range(2,10,3)
for v in values2:
    print(v)