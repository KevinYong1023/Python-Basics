import os

file = open("C:/Users/Kevin/Desktop/Text.txt", "a")
file.write("Text 4 !!")
file.close()

file = open("C:/Users/Kevin/Desktop/Text.txt", "r")
print(file.read())
file.close()


