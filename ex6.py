# Define a variable with an integer value
types_of_people = 10

# Use an f-string to embed the variable in a string
x = f"There are {types_of_people} types of people."

# Define string variables
binary = "binary"
do_not = "don't"

# Use f-strings to embed the string variables in another string
y = f"Those who know {binary} and those who {do_not}."

# Print the value of x and y
print(x)
print(y)

# Print a string that includes the value of x
print(f"I said: {x}")

# Print a string that includes the value of y, with single quotes around y
print(f"I also said: '{y}'")

# Define a boolean variable
hilarious = False

# Define a string with a placeholder
joke_evaluation = "isn't that joke so funny?! {}"

# Use the format method to insert the value of hilarious into the placeholder
print(joke_evaluation.format(hilarious))

# Define two string variables
w = "This is the left side of..."
e = "a string with a right side."

# Concatenate the two strings and print the result
print(w + e)
