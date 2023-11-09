
# Get user input
principal = float(input("Enter the initial principal: "))
interest_rate = float(input("Enter the interest rate: "))
time_periods = int(input("Enter the number of time periods: "))

# Calculate simple interest
simple_interest = principal * (1 + (interest_rate * time_periods))

# Calculate compound interest
compound_interest = principal * (1 + interest_rate) ** time_periods

# Display the results
print("Yusuf and Sons")
print("Simple Interest:", simple_interest)
print("Compound Interest:", compound_interest)
