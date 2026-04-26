**Inventory Copy Behavior and Data Mutation Analysis System**

Department of Computer Science and Engineering

SRM University–AP

Course Code: CSE205 – Hands on Python

Faculty: Dr. Yasir Afaq

**Overview**
------------

This project analyzes how inventory data behaves when it is copied and modified.

The program creates shallow and deep copies of inventory data, applies mutations, and checks whether the original data is affected.

It helps in understanding real-world data corruption issues caused by improper copying.

**Problem Statement**
---------------------

Each inventory item contains price, stock, and supplier rating.

The system must:

Store inventory using nested dictionary structure

Create shallow and deep copies

Modify copied data

Compare original and modified data

Detect whether original data is affected

Generate a final summary

**Inventory Structure**
-----------------------

Each item is stored as:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {"item": "Laptop","details": {"price": 50000, "stock": 10, "supplier_rating": 4.5}}   `

**Approach**
------------

Accepted full roll number as input

Extracted numeric part from roll number

Stored inventory as list of dictionaries

Created shallow copy using .copy()

Created deep copy using copy.deepcopy()

Created backup using deep copy before mutation

Applied mutation using function:

Reduced price by 10%

Reduced stock by 2

Used roll number rule to select index

Compared:

Backup vs shallow copy

Backup vs deep copy

Backup vs original

Stored results in tuple

**Custom Mutation Rule**
------------------------

Index is selected using:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   index = roll_number % length   `

Only that index item is modified.

**Mutation Logic**
------------------

For selected item:

Price is reduced by 10%

Stock is reduced by 2

Changes are applied only on copied data

**Analysis**
------------

Compared original and modified data

Counted number of changed and unchanged items

Stored result as tuple:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   (changed_items, unchanged_items)   `

**Copy Behavior Understanding**
-------------------------------

Shallow copy only copies the outer list

Inner dictionaries are shared

So changes in shallow copy affect original data

Deep copy creates separate memory

So original data remains unchanged

**Program Features**
--------------------

Uses list to store inventory

Uses dictionary for nested structure

Uses functions for modular design

Uses shallow and deep copy

Uses loops and conditions

Uses tuple for summary

Provides clear output

**Sample Test Case**
--------------------

Input:Roll Number: AP24110011614

Behavior:

Target index is calculated

Selected item is modified

Shallow copy affects original

Deep copy remains independent

Tuple summary is generated

**Output Summary Includes**
---------------------------

Original inventory

Shallow copy result

Deep copy result

Differences observed

Tuple summary (changed, unchanged)

Final explanation

**Learning Outcome**
--------------------

From this project, I learned:

How shallow and deep copy work

How nested data behaves during copying

How to detect unintended data changes

How to compare structured data

How to implement real-world logic using Python

**Declaration**
---------------

This submission is my original work.The logic and implementation are based on my own understanding.
