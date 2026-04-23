**Multi-Dimensional Academic Intelligence System**
==================================================

Student Performance Analysis and Classification System

Department of Computer Science and EngineeringSRM University–APCourse Code: CSE205 – Hands on PythonFaculty: Dr. Yasir Afaq

**Overview**
------------

This project analyzes student performance using marks, attendance, and assignment scores.

The program generates student data, classifies students into categories, performs statistical analysis, and detects overall system performance.

**Problem Statement**
---------------------

Each student record contains marks, attendance, and assignment score.

The system must:

*   Generate student data using random values
    
*   Store data in structured format
    
*   Classify students into categories
    
*   Perform statistical analysis
    
*   Detect patterns and generate final system status
    

**Student Classification Rules**
--------------------------------

marks < 40 OR attendance < 50 → At Risk

marks 40 to 70 → Average

marks 71 to 90 → Good

marks > 90 AND attendance > 80 → Top Performer

**Approach**
------------

Accepted last digit of roll number as input

Generated student data using random values

Stored student data as tuples inside a list

Converted data into a Pandas DataFrame

Classified students using conditions

Stored categorized data in a dictionary

Calculated statistics using NumPy:

*   Mean
    
*   Median
    
*   Standard Deviation
    

Calculated mean manually using loop

Calculated correlation between marks and attendance

Normalized marks using list comprehension

Stored summary in a tuple

Used set to store unique student IDs

**Pattern Detection**
---------------------

Consistency → standard deviation < 15

Attendance Risk → more than 3 students have attendance < 50

High Achievement → at least 2 top performers

**System Decision Logic**
-------------------------

Stable Academic SystemIf consistency is good and attendance risk is low

Critical Attention RequiredIf many students have low attendance

Moderate PerformanceIf neither condition is strongly satisfied

**Program Features**
--------------------

Uses lists to store student records

Uses tuples for each student

Uses dictionary for classification

Uses set for unique IDs

Uses NumPy for calculations

Uses Pandas DataFrame for structured data

Uses math module for performance index

Uses list comprehension for normalization

Uses functions for modular design

Generates clear output with analysis

Includes visualization of marks trend

**Performance Index**
---------------------

performance\_index = (marks \* 0.6 + assignment \* 0.4) \* log(attendance + 1)

Marks are given higher weight as they represent main performance

Assignment contributes to continuous evaluation

Log of attendance rewards consistency without making values too large

**Sample Test Case**
--------------------

Input:Last digit of roll number: 4

Behavior:

Student data is generated

First 4 students are selected for analysis

Students are classified into categories

Statistical values are calculated

System status is determined

**Output Summary Includes**
---------------------------

Filtered student DataFrame

Student categories

Mean, Median, Standard Deviation

Correlation between marks and attendance

Summary tuple (mean, std\_dev, max\_marks)

Final system status

Total unique students

**Learning Outcome**
--------------------

From this project, I learned:

How to work with structured data using Pandas

How to perform calculations using NumPy

How to classify data using conditions

How to normalize data using formulas

How to detect patterns using multiple conditions

How to organize code using functions

**Declaration**
---------------

This submission is my original work.The logic and implementation are based on my own understanding.
