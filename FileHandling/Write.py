import os

file = open("C:/Users/Kevin/Desktop/Text.txt", "w")
file.write("Text 5 !!")
file.close()

file = open("C:/Users/Kevin/Desktop/Text.txt", "r")
print(file.read())
file.close()
