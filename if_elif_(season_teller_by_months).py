month = input("Enter a month : ").capitalize()

if month in ["December", "January", "February"]:
    season = "Winter"
elif month in ["March", "April", "May"]:
    season = "Spring"
elif month in ["June", "July", "August"]:
    season = "Summer"
elif month in ["September", "October", "November"]:
    season = "Autumn"
else:
    print("Invalid input. Please enter a valid month.")
    season = None

if season:
    print(f"The season for {month} is {season}.")
