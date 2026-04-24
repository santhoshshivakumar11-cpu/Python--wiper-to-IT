# Day 6: While loop - Code that repeats
password = ""

while password != "ship123":
    password = input("Enter ship password: ")
    if password != "ship123":
        print("Wrong password. Try again.")

print("Access granted! Welcome to Engine Room 🚢")