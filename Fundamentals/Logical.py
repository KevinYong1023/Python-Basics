price = 25
# And operator: check is the both condition are correct, if one wrong, it returns False
print(price > 10 and price < 30)
# Or operator: check is either of the condition are correct, if one wrong, it still can return true if one of them is
# correct
print(price > 10 or price < 30)

# If-Else Statement
temperature = int(input("Enter a temperature: "))
if temperature < 30:
    print("Good day")
elif 30 < temperature < 35:
    print("Normal day")
else:
    print('Not a good day')

#  Exercise
weight = float(input("Weight: "))
unit = input("Kg or Lbs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs:", converted)
elif unit.upper() == "L":
    converted = weight * 0.45
    print("Weight in Kg:", converted)
else:
    print("Please entered a correct unit")
