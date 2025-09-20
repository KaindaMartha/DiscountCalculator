def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
input_price = float(input("Enter the original price: "))
input_discount = float(input("Enter the discount percentage: "))
final_price = calculate_discount(input_price, input_discount)
print(f"The final price after discount is: {final_price:.2f}")

