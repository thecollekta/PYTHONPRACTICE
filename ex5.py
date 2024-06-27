name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_2 = height * 2.54
weight_2 = weight / 0.45 #kg

print(f"Let's talk about my {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eys and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the co")
      
# this line is tricky, try to get it exactly right
total = age + height + weight
total_2 = age + height_2 + weight_2
print(f"If I add {age}, {height}, and {weight} I get {total}")

print(f"If I add {age}, {height_2}, and {weight_2} I get {total_2}")
