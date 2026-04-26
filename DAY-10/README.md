📘 **Academic Data Drift & Copy Behavior Analyzer**
===================================================

**Student Data Mutation and Drift Detection System**

Department of Computer Science and Engineering

SRM University–AP

Course Code: CSE205 – Hands on Python

Faculty: Dr. Yasir Afaq

**Overview**
------------

This project analyzes how student data behaves when it is copied and modified.

The program creates shallow and deep copies of student data, applies mutations, and checks whether the original data is affected.

It also calculates statistical changes (data drift) and classifies the system based on those changes.

**Problem Statement**
---------------------

Each student record contains marks, attendance, and scores.

The system must:

Generate student data using random values

Store data in nested dictionary format

Create shallow and deep copies

Apply mutations to copied data

Perform statistical analysis

Detect data drift

Identify copy failure

Generate final system status

**Data Structure**
------------------

Each student record is stored as:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {"id": int,"marks": int,"attendance": int,"scores": [internal, assignment]}   `

**Approach**
------------

Accepted full roll number as input

Extracted numeric part from roll number

Generated 10–15 students using random

Stored data as list of dictionaries

Converted data into Pandas DataFrame

Created:

*   shallow copy
    
*   deep copy
    

Created backup using deep copy before mutation

Applied mutation only on copied data:

*   increased marks using sqrt
    
*   modified scores list
    
*   reduced attendance
    

Used roll number rule to select indexes

Performed analysis using NumPy:

*   mean
    
*   median
    
*   standard deviation
    

Calculated mean manually using loop

Normalized marks using list comprehension

Calculated drift between original and modified data

Checked whether original data was affected

Generated final system classification

**Custom Mutation Rule**
------------------------

Indexes are selected using:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   rule_value = roll_number % 3   `

If it becomes 0, it is set to 1.

Mutation is applied where:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   index % rule_value == 0   `

**Mutation Logic**
------------------

For selected students:

Marks increased using square root

Scores list modified (first value increased)

Attendance reduced

Changes applied only on copied data

**Analysis**
------------

Calculated:

Mean

Median

Standard Deviation

Manual Mean using loop

Unique values using set

Normalized marks using:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   (x - min) / (max - min)   `

**Drift Detection**
-------------------

Drift is calculated as:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   abs(original_mean - modified_mean)   `

Custom threshold used:

Small drift → Stable Data

Medium drift → Minor Drift

High drift → Critical Drift

**Pattern Detection**
---------------------

Copy Failure → if original data changes

Drift Status → based on drift value

Final Status → combination of both

**Copy Behavior Understanding**
-------------------------------

Shallow copy only copies outer structure

Inner lists (scores) are shared

So modifying shallow copy affects original data

Deep copy creates fully independent data

So original data remains unchanged

**Program Features**
--------------------

Uses list to store data

Uses dictionary for nested structure

Uses set for unique values

Uses functions for modular design

Uses NumPy for calculations

Uses Pandas DataFrame

Uses math module for transformation

Uses shallow and deep copy

Uses list comprehension

Provides structured output

**Sample Test Case**
--------------------

Input:Roll Number: AP24110011614

Behavior:

Students are generated

Mutation rule is applied

All indexes get modified

Shallow copy affects original

Deep copy remains independent

Drift is calculated

Final status is generated

**Output Summary Includes**
---------------------------

Original DataFrame

Shallow copy result

Deep copy result

Drift value

Summary tuple (mean, drift, std\_dev)

Final system status

**Learning Outcome**
--------------------

From this project, I learned:

How shallow and deep copy behave differently

How data drift occurs during modification

How to use NumPy and Pandas together

How to apply custom rules using roll number

How to analyze and compare structured data

**Declaration**
---------------

This submission is my original work.The logic and implementation are based on my own understanding.
