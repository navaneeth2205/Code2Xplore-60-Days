#program to validate credentials for approving a  student account
student_id=input("Enter Student ID:")
email=input("Enter Email ID:")
Password=input("Enter Password:")
referral=input("Enter Referral Code:")

#student ID verification
if len(student_id)==7 and student_id[0]=="C" and student_id[1]=="S" and student_id[2]=="E" and student_id[3]=="-" and student_id[4].isdigit() and student_id[5].isdigit() and student_id[6].isdigit():

    #email id verification
    if email.count('@')>=1 and email.count('.')>=1 and email[0]!="@" and email[-4]=="." and email[-3]=="e" and email[-2]=="d" and email[-1]=="u":

        #Password validation
        if len(Password)>=8 and Password[0].isupper() and Password.count("0")>=1 or Password.count("1")>=1 or Password.count("2")>=1 or Password.count("3")>=1 or Password.count("4")>=1 or Password.count("5")>=1 or Password.count("6")>=1 or Password.count("7")>=1 or Password.count("8")>=1 or Password.count("9")>=1:

            #Referral Code rules
            if len(referral)==6 and referral[0]=="R" and referral[1]=="E" and referral[2]=="F" and referral[3].isdigit() and referral[4].isdigit() and referral[5]=="@":
                print("APPROVED")
            else:
                print("REJECTED")
        else:
            print("REJECTED")
    else:
        print("REJECTED")
else:
    print("REJECTED")