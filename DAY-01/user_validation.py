# Program to validate a user before using university web portal

name=input("Enter your full name:")
email=input("Enter your email id:")
mobile_number=input("Enter your mobile number:")
age=int(input("Enter your age:"))

#full name validation
if name.count(" ")>=1 and name[0]!=" "  and name[len(name)-1]!=" ":

    #email Id validation
    if email.count("@")==1 and email.count(".")==1 and email[0]!="@":

        #mobile number verification
        digit_check=mobile_number.replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","")
        if len(mobile_number)==10 and len(digit_check)==0 and mobile_number[0]!="0":  # digit_check logic is done by replacing every digit with a empty string , if length after replacing is zero then it only contains digits

            #age validation
            if age>=18 and age<=60:
                print("User Profile is VALID")

            else:
                print("User Profile is INVALID")
        else:
            print("User Profile is INVALID")
    else:
        print("User Profile is INVALID")
else:
    print("User Profile is INVALID")