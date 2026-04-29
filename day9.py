def check_fuel(fuel_level):
    if fuel_level > 20:
        print("Fuel is okay. Engine running.")
    else:
        print("Warning: Low fuel!")

# Call the function
check_fuel(85)  # Output: Fuel is okay. Engine running.
check_fuel(20)  # Output: Warning: Low fuel!