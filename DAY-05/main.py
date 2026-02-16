rsrc_requests=[]
n=int(input("Enter Number of requests: "))
for i in range(n):
    request=int(input(f"Enter a resource request {i+1}: "))
    rsrc_requests+=[request]

low_demand=[]
moderate_demand=[]
high_demand=[]
invalid_request=[]
no_demand=0
invalid=0
removed=0
for request in rsrc_requests:
    if request<0:
        invalid_request+=[request]
        invalid+=1
    elif request==0:
        no_demand+=1
    elif request<=20:
        low_demand+=[request]
    elif request<=50:
        moderate_demand+=[request]
    else:
        high_demand+=[request]

name=input("Enter your full name: ")
L=len(name.replace(" ",""))
PLI=L%3

print(f"Length of the Name excluding spaces(L): {L}")
print(f"PLI: {PLI}")

print("\nLow Demand: ",low_demand)
print("Moderate Demand: ",moderate_demand)
print("High Demand: ",high_demand)
print("Invalid Request/s: ",invalid_request)

if PLI==0:
    removed+=len(low_demand)
    low_demand=[]
elif PLI==1:
    removed+=len(high_demand)
    high_demand=[]
else:
    removed+=len(low_demand)+len(high_demand)
    low_demand=[]
    high_demand=[]

print("\nAfter Personalization: ")
print("Low Demand: ",low_demand)
print("Moderate Demand: ",moderate_demand)
print("High Demand: ",high_demand)
print("Invalid Request: ",invalid_request)

print("\nRemoved After Personalization: ",removed)
print("Total Valid requests: ",len(rsrc_requests)-invalid)
print("Total Invalid requests: ",invalid)
print("Requests with No Demand: ",no_demand)