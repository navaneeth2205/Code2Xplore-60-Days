transaction_amounts=[]
n=int(input("Enter number of transactions: "))
for i in range(0,n):
    transaction_amounts.append(int(input(f"Enter transaction {i+1}: ")))
normal=[]
large=[]
high_risk=[]
invalid=[]

for amount in transaction_amounts:
    if amount<=0:
        invalid.append(amount)
    elif amount<=500:
        normal.append(amount)
    elif amount<=2000:
        large.append(amount)
    else:
        high_risk.append(amount)


categorized_transactions={
    "normal":normal,
    "large":large,
    "high_risk":high_risk,
    "invalid":invalid
}

print("\nCategorized Transactions",categorized_transactions)

count=len(transaction_amounts)
sum_transactions=sum([i for i in transaction_amounts if i>0])
summary=(sum_transactions,count)

print("Total Transaction value = ",summary[0])
print("Number of transactions = ",summary[1])

frequent_transaction=count>5
large_spending=sum_transactions>5000
suspicious=len(high_risk)>=3

print("Risk Classification: ",end="")
if suspicious or (frequent_transaction and large_spending):
    print("High Risk")
elif frequent_transaction or large_spending:
    print("Moderate Risk")
else:
    print("Low Risk")