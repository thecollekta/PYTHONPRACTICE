# Mad Libs Story Generator

# Prompt user for different words
adjective1 = input("Enter the first adjective: ")
adjective2 = input("Enter the second adjective: ")
adjective3 = input("Enter the third adjective: ")
adjective4 = input("Enter a final adjective: ")

# Conditional vartiations
if adjective1 == "handsome":
    start_sentence = "On a truly fantastic day, I went to the zoo."
else:
    start_sentence = f"On a {adjective1} day, I went to the zoo."

# Telling the story with the user input
Mad_Libs_Story =  ( 
    f"{start_sentence} "
    f"I saw a funny {adjective2} moneky swinging from the tree. "
    f"Then, I spotted a majestic {adjective3} lion lounging in the sun. "
    f"What a wild and {adjective4} experience!")

print(Mad_Libs_Story)