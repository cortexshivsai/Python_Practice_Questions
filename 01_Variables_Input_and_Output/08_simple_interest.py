#Calculate simple interest
principal_amt=int(input("Enter the principal amount: "))
rate_of_interest=float(input("Enter rate of interest(in percentage): "))
time_period=int(input("Enter Time Period(in years): "))
simple_interest=(principal_amt*rate_of_interest*time_period)/100
print(f"The simple interest is: {simple_interest}")
print(f"The total amount with interest is: {principal_amt+simple_interest}")