University Grade Calculation System
===================================

CSE205 – Hands on PythonSRM University–AP

Challenge Understanding
-----------------------

In this DAY-3 challenge, we had to design a system that calculates the grades of university students based on the internal marks they score.

First, we need to take marks from the user and store them in a list. Then we process each mark one by one and assign a grade according to the given conditions. We also need to count how many students are valid and how many have failed.

Additionally, we must apply personalization so that the output becomes unique. For personalization, we can use our name, registration number, or section to modify some part of the logic. This makes each student’s output slightly different.

How the Program Works
---------------------

*   The program accepts a list of marks from the user.
    
*   It uses a loop to go through each mark.
    
*   Based on conditions, it assigns grades like:
    
    *   Excellent
        
    *   Very Good
        
    *   Good
        
    *   Average
        
    *   Fail
        
*   If the mark is invalid (less than 0 or more than 100), it is marked as Invalid.
    
*   It keeps track of:
    
    *   Total valid students
        
    *   Total failed students
        
*   Personalization logic is applied to slightly adjust or influence the grading output.
    

Test Case Verification
----------------------

### Test Case 1

Input:marks = \[95, 82, 67, 45, 30\]

Output:Mark: 95 → ExcellentMark: 82 → Very GoodMark: 67 → GoodMark: 48 → AverageMark: 30 → Fail

Total Valid Students: 5Total Failed Students: 1

### Test Case 2

Input:marks = \[110, -5, 70, 39\]

Output:Mark: 110 → InvalidMark: -5 → InvalidMark: 70 → GoodMark: 39 → Fail

Total Valid Students: 2Total Failed Students: 1

### Test Case 3

Input:marks = \[103, 36, 85, 99, 72, 64\]

Output:Mark: 103 → InvalidMark: 40 → AverageMark: 85 → Very GoodMark: 99 → ExcellentMark: 75 → Very GoodMark: 64 → Good

Total Valid Students: 5Total Failed Students: 0

Learning Outcome
----------------

From this challenge, I learned how to work with lists and apply loops properly.I improved my understanding of conditional statements for classification.I also understood how personalization techniques can be applied using my name length or other personal data to make the program output unique.

This challenge helped me strengthen my logic-building skills in Python.
