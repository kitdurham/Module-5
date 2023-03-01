# HOMEWORK MODULE 5 PART 2

# Create a list named food with two elements 'rice' and 'beans' and use print() to verify.
food = ['rice', 'beans']
print(food)

# Append the string 'broccoli' to food using .append() and use print() to verify.
food.append('broccoli') 
print(food)

# Add the strings 'bread' and 'pizza' to food using .extend() and use print() to verify.
food.extend(['bread', 'pizza'])
print(food)

# Print the first two items in the food list using print() and slicing notation.
print(food[0:2])

# Print the last item in food using print() and index notation.
print(food[-1])

# Create a list called breakfast from the string "eggs,fruit,orange juice" using the split() method.
breakfast_string = "eggs,fruit,orange juice"
breakfast = breakfast_string.split(",")
print(breakfast)

# Verify that breakfast has 3 elements using the len built-in.
print(len(breakfast))

# prompt the user for a floating-point value until they enter stop. Store the entries in a list, then find average, min, and max of their entries and print those values.
numbers = []
while True:
    user_input = input("Enter a floating-point value or 'stop' to exit: ")
    if user_input == 'stop':
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Enter a floating-point value or 'stop' to exit.")
if numbers:
    average = sum(numbers) / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    print("Average:", average)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
else:
    print("No values were entered.")
