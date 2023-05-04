income_of_client = input("Share your income (high / low): ")
credit_of_client = input("Share your credit (good / bad): ")


if income_of_client == "high" and credit_of_client == "good":
    print("You are eligible of loan")
else:
    print("You are not eligible of loan")