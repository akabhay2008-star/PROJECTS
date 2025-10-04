# Online Shopping Checkout - Simplified Payment Calculation

# Step 1: Input item prices and quantities
items = {"Shoes": 2000, "T-shirt": 500, "Jeans": 1500}
quantities = {"Shoes": 1, "T-shirt": 2, "Jeans": 1}

# Step 2: Calculate subtotal
subtotal = 0
for item in items:
    subtotal += items[item] * quantities[item]

print("Subtotal:", subtotal)

# Step 3: Apply discount
discount_code = input("Enter discount code (SAVE10 for 10% off): ")
if discount_code == "SAVE10":
    discount = subtotal * 0.10
else:
    discount = 0

total = subtotal - discount
print("Total after discount:", total)

# Step 4: Payment method
payment_method = input("Enter payment method (Card/UPI/Cash): ")
if payment_method in ["Card", "UPI", "Cash"]:
    print("Payment Successful via", payment_method)
    print("Receipt Generated. Thank you for shopping!")
else:
    print("Invalid Payment Method. Please try again.")
