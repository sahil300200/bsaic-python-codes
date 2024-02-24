principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest per annum: "))
time_period = float(input("Enter the time period in years: "))
simple_interest = (principal * rate_of_interest * time_period) / 100
compound_interest = principal * (1 + rate_of_interest/100)**time_period - principal
print(f"Simple Interest: {simple_interest}")
print(f"Compound Interest: {compound_interest}")
