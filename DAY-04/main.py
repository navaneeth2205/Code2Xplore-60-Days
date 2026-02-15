#Cyber Activity Risk Analyzer
n=int(input("Enter number of students: "))
Scores=[]
for i in range(0,n):
    score=int(input(f"Enter a activity intensity score for student {i}: "))
    Scores+=[score]
low_risk=[]
medium_risk=[]
high_risk=[]
critical_risk=[]
ignored=0

for i in range(0,n):
    if Scores[i]<0:
        ignored+=1
    elif Scores[i]<=30:
        low_risk+=[Scores[i]]
    elif Scores[i]<=60:
        medium_risk+=[Scores[i]]
    elif Scores[i]<=100:
        high_risk+=[Scores[i]]
    else:
        critical_risk+=[Scores[i]]


reg_no = input("Enter your register number: ")
D = int(reg_no[len(reg_no)-1])
print(f"Register Digit (D): {D}\n")

#printing Before personalization
print("Low Risk: ",low_risk)
print("Medium Risk: ",medium_risk)
print("High Risk: ",high_risk)
print("Critical Risk: ",critical_risk)

#Personalized Security Filter
if D % 2 == 0:
    personalized = len(low_risk)
    low_risk = []
else:
    personalized = len(critical_risk)
    critical_risk = []


print("\nAfter Personalized Filtering:")
print("Low Risk: ",low_risk)
print("Medium Risk: ",medium_risk)
print("High Risk: ",high_risk)
print("Critical Risk: ",critical_risk)

print("\nTotal Valid Entries: ",n-ignored)
print("Ignored Entries: ",ignored)
print("Removed Due to Personalization: ",personalized)