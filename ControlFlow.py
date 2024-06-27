# def weekday(n):
#     match n:
#         case 1: return "Monday"
#         case 2: return "Tuesday"
#         case 3: return "Wednesday"
#         case 4: return "Thursday"
#         case 5: return "Friday"
#         case 6: return "Saturday"
#         case _: return "Invalid day number"
# print(weekday(3))
# print(weekday(6))
# print(weekday(7))

# def access(user):
#     match user:
#         case "admin" | "manager": return "Full access"
#         case "Guest": return "Limited access"
#         case _: return "No access"
# print(access("manager"))
# print(access("Guest"))
# print(access("Ravi"))

from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)