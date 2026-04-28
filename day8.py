crew_members = ["Ravi", "Arun", "Sandeep"]

for member in crew_members:
    print(f"Checking {member} on duty")
    
    fuel_level = 100

while fuel_level > 20:
    print(f"Fuel at {fuel_level}% - Running")
    fuel_level -= 15  # reduce fuel by 15 each time