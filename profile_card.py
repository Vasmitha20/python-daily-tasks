# Formatted Profile Card

# Ask the user for details
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
fav_sub = input("Enter your favourite subject: ")

# Calculating the birth year
birth_yr = 2026 - age

# Displaying the profile card
print("\n========== PROFILE CARD ==========")
print(f"Name              : {name}")
print(f"Age               : {age}")
print(f"City              : {city}")
print(f"Favourite Subject : {fav_sub}")
print(f"Birth Year        : {birth_yr}")
print("====================================")