***Challenge Understanding***
Briefly explain the problem statement of the DAY-2 challenge in your own words.
	The problem is to design and implement a credential validation system for approving a student account in a university registration system. Before approving the account, the system must verify student ID, email ID, password, and referral code using given rules. If all the details satisfy the conditions, the account is approved, otherwise it is rejected.

***Validation Rules Implemented***
Student ID Validation:
 I validated the student ID by checking its format as CSE-XXX. I used len() and indexing to check whether it starts with “CSE”, the fourth character is ‘-’, and the last three characters are digits.
Email ID Validation:
 I validated the email ID using count() and indexing. I checked whether the email contains ‘@’ and ‘.’, ensured that ‘@’ is not the first character, and verified that the email ends with “.edu”.
Password Validation:
 I validated the password by checking its length using len(), ensuring the first character is an uppercase letter, and confirming that it contains at least one digit using count().
Referral Code Validation:
 I validated the referral code by checking the format REF##@. I used len(), indexing, and isdigit() to ensure it starts with “REF”, followed by two digits, and ends with ‘@’.

***Approach / Logic Used***
Describe the logic used to solve the problem using strings and conditions.
	The program uses string functions like len(), count(), isdigit(), and indexing along with conditional statements. I used nested if-else blocks to validate each input one by one. If any validation fails, the program prints REJECTED immediately. Only when all conditions are satisfied, the program prints APPROVED.
  
***Algorithm / Steps***
Write the step-by-step algorithm followed to solve the challenge.
Take inputs for student_id, email, password, and referral code from the user.
Validate the student ID format using string indexing and digit checks.
Validate the email ID using count() and indexing and check if it ends with “.edu”.
 Validate the password for minimum length, uppercase first character, and at least one digit.
 Validate the referral code format using indexing and digit checks.
 If all conditions are satisfied, print “APPROVED”.
 Else print “REJECTED”.
