Emergency Resource Dispatch Analyzer
====================================

Department of Computer Science and EngineeringSRM University–APCourse: CSE205 – Hands on PythonFaculty: Dr. Yasir Afaq

Project Overview
----------------

This project analyzes emergency resource requests reported during a disaster drill.

Each zone sends the number of resources it needs. Some requests may be invalid or unrealistic.The program classifies these requests into different demand levels and applies a personalized filtering rule based on the length of my name.

Finally, it generates a structured dispatch report.

Problem Description
-------------------

Each resource request is an integer value.

The program performs the following steps:

*   Identifies invalid requests (negative values)
    
*   Detects zones with no demand (value = 0)
    
*   Categorizes valid requests into:
    
    *   Low Demand (1–20)
        
    *   Moderate Demand (21–50)
        
    *   High Demand (>50)
        
*   Applies a personalized rule using PLI
    
*   Displays the final categorized lists and summary counts
    

Classification Rules
--------------------

Request Value Classification

*   Less than 0 → Invalid Request
    
*   0 → No Demand
    
*   1–20 → Low Demand
    
*   21–50 → Moderate Demand
    
*   Greater than 50 → High Demand
    

Personalization Logic
---------------------

L = Length of my full name excluding spacesPLI = L % 3

My full name: Navaneeth Biyyapu

Length excluding spaces (L) = 18PLI = 18 % 3 = 0

Since PLI = 0, Rule A is applied:

All Low Demand requests are removed from the final report.

Program Features
----------------

*   Uses lists for categorization
    
*   Uses for loops for processing
    
*   Uses conditional statements for classification
    
*   Separates invalid data properly
    
*   Applies personalized filtering logic
    
*   Generates a final dispatch summary
    

Sample Input
------------

\[10, 25, 60, -3, 0, 45, 80\]

Sample Output Behavior (For PLI = 0)
------------------------------------

Low Demand: \[\]Moderate Demand: \[25, 45\]High Demand: \[60, 80\]Invalid Request: \[-3\]

Removed After Personalization: 1Total Valid Requests: 6Total Invalid Requests: 1Requests with No Demand: 1

Learning Outcome
----------------

From this project, I learned:

*   How to process lists using loops
    
*   How to classify data using conditional logic
    
*   How to separate invalid and valid inputs
    
*   How to apply personalized filtering using modulo operation
    
*   How to generate structured output reports
    

Declaration
-----------

This project is my own original work.The personalization logic is based on my name length.All logic and implementation were written and understood by me.
