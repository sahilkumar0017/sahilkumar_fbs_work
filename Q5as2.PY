cost_price = float(input("Enter cost price of book: "))
discount_percent = float(input("Enter discount percentage: "))

# Calculate discount amount
discount = (cost_price * discount_percent) / 100

# Calculate selling price
selling_price = cost_price - discount

# Display result
print("Discount Amount:", discount)
print("Selling Price:", selling_price)
