import os

file = open("C:/Users/Kevin/Desktop/Text.txt", "r")
print("file.read()", file.read())  # print the text file
print("file.read(2)", file.read(2))  # print the first two character
file.close()
f = open("C:/Users/Kevin/Desktop/Text.txt", "r")
print("f.readLines()", f.readlines())  # list containing each line in the file as a list item
f.close()