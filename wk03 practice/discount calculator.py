amount=float(input("Amount: "))
if amount <0:
    print("Amount cannot be less than 0")

elif amount>0 and amount <10000:
    discount=0
    price=amount
    
elif amount >=10000 and amount <50000:
     discount=(5/100)*amount
     price=amount-discount

else:
    discount=(10/100)*amount
    price=amount-discount

print("Summary")
print()
print("Original amount is",amount)
print("Discount amount is",discount)
print(f"Final amount is {price}")
