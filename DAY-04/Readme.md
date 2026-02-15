Cyber Activity Risk Analyzer
============================

Personalized Security Engine

Department of Computer Science and EngineeringSRM University–APCourse Code: CSE205 – Hands on PythonFaculty: Dr. Yasir Afaq

Overview
--------

This project analyzes student login activity intensity scores to determine different risk levels.

The program cleans invalid data, categorizes valid scores into risk groups, applies a personalized security filter based on the last digit of my register number, and generates a final summary report.

Problem Statement
-----------------

Each login session generates an integer activity intensity score.

The system must:

*   Ignore invalid negative values
    
*   Categorize valid scores into risk levels
    
*   Apply a personalized filtering rule
    
*   Display a structured final report
    

### Risk Classification Rules

*   Score < 0 → Ignored
    
*   0 to 30 → Low Risk
    
*   31 to 60 → Medium Risk
    
*   61 to 100 → High Risk
    
*   Above 100 → Critical Risk
    

Approach
--------

*   Accepted the number of students as input
    
*   Collected activity scores using a for loop
    
*   Processed each score using conditional statements
    
*   Stored scores in separate lists:
    
    *   low\_risk
        
    *   medium\_risk
        
    *   high\_risk
        
    *   critical\_risk
        
*   Counted ignored entries
    
*   Extracted the last digit of the register number
    
*   Applied personalized filtering logic
    
*   Displayed categorized lists before and after filtering
    
*   Printed total valid entries, ignored entries, and removed entries
    

Personalization Rule
--------------------

Last digit of my Register Number = 4

Since 4 is even, I removed all Low Risk scores after categorization.

Only Medium, High, and Critical Risk scores remain in the final output.

Program Features
----------------

*   Uses lists for structured data storage
    
*   Uses for loops for processing
    
*   Uses conditional statements for classification
    
*   Implements register-number-based personalization
    
*   Generates a clear summary report
    

Sample Test Case
----------------

Input:10, 45, 78, 120, -5, 30, 99, 150

Behavior:

*   \-5 is ignored
    
*   Low Risk values removed (because D is even)
    
*   Remaining categories displayed
    
*   Summary counts shown correctly
    

Output Summary Includes
-----------------------

*   Risk categories before filtering
    
*   Risk categories after filtering
    
*   Total valid entries
    
*   Ignored entries
    
*   Removed entries due to personalization
    

Learning Outcome
----------------

From this project, I learned:

*   How to use lists effectively
    
*   How to process data using loops
    
*   How to apply conditional logic
    
*   How to implement personalized program behavior
    
*   How to generate structured output reports
    

Declaration
-----------

This submission is my original work.The personalization logic is based on my own register number.
