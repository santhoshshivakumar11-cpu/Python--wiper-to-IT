print("=== Engine OT Checker ===")
name = input("Enter crew name: ")
hours = int(input("Enter OT hours this week: "))

if hours > 15:
    extra = hours - 15
    print(f"{name}, OT alert! {extra} hrs over limit")
else:
    left = 15 - hours
    print(f"{name}, OT OK. {left} hrs left")