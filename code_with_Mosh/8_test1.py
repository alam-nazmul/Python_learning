actual_price_of_house = 1000000
buyer_condition = input("Share your credit situation (good / bad): ")

if buyer_condition == "good":
    down_payment = actual_price_of_house * 0.1
    print(f'Your down payment is {down_payment}')
else:
    down_payment = actual_price_of_house * 0.2
    print(f'Your down payment is {down_payment}')