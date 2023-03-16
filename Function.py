def demoFunction(name, age):
    print(name, age)


demoFunction("Kevin", 23)

# We can use in other file as well:
# For example: we can import the function coming from the main.py file
import main
from main import print_hi
from main import print_hi as print_text

main.print_hi("Hey main.print_hi")
print_hi("Hey print_hi")
print_text("Hey print_text")
