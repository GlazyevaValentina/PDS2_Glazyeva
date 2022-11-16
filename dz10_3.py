""""""""""""
# My experiments with Exeptions
""""""""""""
# Example1
#Division by zero, incorrect symbol
print("Example1\nDivision by zero, incorrect symbol")
x = input("x: ")
y = input("y: ")
try:
    x = int(x)
    y = int(y)
    division_result = x / y

except ZeroDivisionError:
    division_result = "Division by zero is impossible"

except ValueError:
    division_result = "One of the entered values is not a number"

print(division_result)

# Example2
# Experiment with classes
print("\nExample2\Experiment with classes")
class Creatures(Exception):
    pass

class Animals(Creatures):
    pass

class Wild_animals(Animals):
    pass
# Correct classes order
print("Correct classes order")
for cls in [Creatures, Animals, Wild_animals]:
    try:
        raise cls()
    except Wild_animals:
        print("Wild animals")
    except Animals:
        print("Animals")
    except Creatures:
        print("Creatures")
# Incorrect classes order
print("\nIncorrect classes order")
for cls in [Creatures, Animals, Wild_animals]:
    try:
        raise cls()
    except Creatures:
        print("Creatures")
    except Animals:
        print("Animals")
    except Wild_animals:
        print("Wild animals")

