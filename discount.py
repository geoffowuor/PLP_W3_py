def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))


final_price = calculate_discount(original_price, discount_percentage)
if final_price != original_price:
    print(f"Final price after discount: {final_price:.2f}")
else:
    print("No discount applied. Final price remains the same.")
