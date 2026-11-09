#Simple interest calculator
principal = float(input("Enter principal:"))
rate = float(input("Enter the rate:"))
time = float(input("Enter the time: "))
interest = (principal * rate * time)/100
final_amount = principal + interest
print(f"Interest: NGN {interest:,.2f}")
print(f"Final Amount: NGN {final_amount:,.2f}")
