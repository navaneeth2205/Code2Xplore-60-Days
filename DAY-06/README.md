Smart Transaction Risk Detector
===============================

### Transaction Analysis and Risk Classification System

**Department of Computer Science and Engineering****SRM University–AP****Course Code:** CSE205 – Hands on Python**Faculty:** Dr. Yasir Afaq

Overview
--------

This project analyzes daily transaction amounts to identify spending patterns and detect risk levels.

The program takes transaction inputs, filters invalid values, classifies transactions into categories, and evaluates patterns to generate a final risk report.

Problem Statement
-----------------

Each transaction is represented as an integer amount.

The system must:

*   Identify invalid transactions
    
*   Categorize valid transactions into risk levels
    
*   Analyze transaction patterns
    
*   Display a structured risk report
    

Transaction Classification Rules
--------------------------------

*   **t ≤ 0** → Invalid Transaction
    
*   **1 to 500** → Normal
    
*   **501 to 2000** → Large
    
*   **Above 2000** → High Risk
    

Approach
--------

*   Accepted number of transactions as input
    
*   Collected transaction amounts using a for loop
    
*   Classified each transaction using conditions
    
*   Stored data in separate lists:
    
    *   normal
        
    *   large
        
    *   high\_risk
        
    *   invalid
        
*   Stored categorized data in a dictionary
    
*   Calculated total transaction value using list comprehension
    
*   Stored summary _(total, count)_ in a tuple
    

### Pattern Detection

*   Frequent transactions _(count > 5)_
    
*   Large spending _(total > 5000)_
    
*   Suspicious activity _(≥ 3 high-risk transactions)_
    
*   Determined final risk level based on these conditions
    

Risk Decision Logic
-------------------

### High Risk

*   If 3 or more high-risk transactions exist
    
*   OR if both frequent transactions and large spending occur
    

### Moderate Risk

*   If only one condition is true
    
    *   frequent transactions
        
    *   OR large spending
        

### Low Risk

*   If none of the conditions are satisfied
    

Program Features
----------------

*   Uses lists for storing transaction data
    
*   Uses loops for processing input
    
*   Uses conditional statements for classification
    
*   Uses dictionary for organized storage
    
*   Uses list comprehension for filtering valid values
    
*   Uses tuple for summary
    
*   Generates a clear and structured output
    

Sample Test Case
----------------

**Input:**

  150, 200, 250, 500, 2000, -50, 985, 50, 100, 120   `

**Behavior:**

*   \-50 is classified as invalid
    
*   Remaining values are categorized properly
    
*   Total and count are calculated
    
*   Risk is classified as **Moderate Risk**
    

Output Summary Includes
-----------------------

*   Categorized transactions
    
*   Total transaction value
    
*   Number of transactions
    
*   Final risk classification
    

Learning Outcome
----------------

From this project, I learned:

*   How to classify data using conditions
    
*   How to use dictionaries for structured storage
    
*   How to apply list comprehension
    
*   How to combine multiple conditions for decision making
    
*   How to build a complete real-world logic-based program
    

Declaration
-----------

This submission is my original work.The logic and implementation are based on my own understanding.
