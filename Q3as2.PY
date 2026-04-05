feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))

# Convert to meters
meters = (feet * 0.3048) + (inches * 0.0254)

# Convert to centimeters
centimeters = meters * 100

# Display result
print("Distance in meters:", meters)
print("Distance in centimeters:", centimeters)