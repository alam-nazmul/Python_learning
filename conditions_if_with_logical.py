applicant_income = input("Please enter your income (high / low): ")
applicant_credit = input("Please enter your credit (high / low): ")
applicant_credit = applicant_credit.lower()
applicant_income = applicant_income.lower()

if applicant_income == "high" and applicant_credit == "high":
    print("You are eligible for loan.")
else:
    print("You are not eligible for loan.")