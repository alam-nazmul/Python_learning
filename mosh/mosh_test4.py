buyer_credit = input("Enter your credit (good / bad ): " )
buyer_credit = buyer_credit.lower()
house_price = 100000

if buyer_credit == "good":
    down_payment = house_price * 0.1
else:
    down_payment = 0.2 * house_price
print(f'Your down payment is {down_payment}')