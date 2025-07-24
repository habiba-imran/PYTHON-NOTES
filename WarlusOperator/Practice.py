# := It allows you to assign a value to a variable as part of an expression.
a = True # though a is true initially but we have initialized it again in print
print(a := False) # prints false

foods = list() # empty list of food
while (food := input("What food do you like? ")) != "quit":
    foods.append(food)
print(foods)

if (n := len("Habiba")) > 5:
    print(f"Length is {n}, which is greater than 5.")

# Continue looping while user input is not empty
while (user_input := input("Enter something: ")) != "":
    print(f"You typed: {user_input}")




