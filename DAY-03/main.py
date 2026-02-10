n=int(input("Enter the number of students: "))
marks=[0]*n
for i in range(n):
    marks[i]=(int(input(f"Enter marks of the students {i+1}:")))# Assumed students are started from 1....

#Personalization based on name
# name="navaneeth"
# name.length=9
# so if a marks are divisible by 9 , add +3 , if after adding marks are 39 then add one and make the student as pass , and if after adding marks are greater than 100 don't add +3 to the mark.
valid=0
failed=0
for mark in marks:
    if 0<=mark<=100:
        valid+=1
        if mark%9==0:
            mark+=3
            if mark==39:
                mark=40
            if mark>100:
                mark-=3
        if 0<=mark<=39:
            print(f"Mark: {mark} -> Fail")
            failed+=1
        elif 40<=mark<=59:
            print(f"Mark: {mark} -> Average")
        elif 60<=mark<=74:
            print(f"Mark: {mark} -> Good")
        elif 75<=mark<=89:
            print(f"Mark: {mark} -> Very Good")
        else:
            print(f"Mark: {mark} -> Excellent")
    else:
        print(f"Mark: {mark} -> Invalid")
print(f"Total Valid Students: {valid}")
print(f"Total Failed Students: {failed}")

