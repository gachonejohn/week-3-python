def calculate_discount(price, discount_percent):
    if discount_percent >= 20:      
        discount_amount = price * (discount_percent / 100)
        
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# prompting the user to input price and discount percentage 
price = float(input("Enter the original price of the item: ksh "))
discount_percent = float(input("Enter the discount percentage: "))

# calculating  the final price after applying the discount
final_price = calculate_discount(price, discount_percent)

# Print the final price or the original price if no discount was applied
if final_price == price:
    print(f"No discount applied. The price remains: Ksh{final_price:.2f}")
else:
    print(f"The final price after applying the discount is: Ksh{final_price:.2f}")
