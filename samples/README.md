# Code Formatting Rules
=====================================

## 1. File Seperation
-------------------------------
Small files are easier to understand more than large files.
Seperate files for each functionality, and call them in the main file.

## 2. Function/Loop Variables definition
-------------------------------
Function/loop variables decleration should be at the top of the function/loop itself not the top of the file.
*Clean Code Page 81*


## 3. Minutia
-------------------------------
Each file should have a README.md file that explains the purpose of the file/function/code and how to use it.


## 4. Calling
-------------------------------
1. Fuctions should be called at the end of the function itself, not at the top of the file.

2. The caller function should be above the calle.

3. Caller and Callee should be clossed.
*Clean Code Page 81*

## 5. Concepunal affinity
-------------------------------
Group affinity functions together in the same file.

## 6. Code Structure
-------------------------------
Your code should be read like an article, Top-Down narative.
At the top of the file, explain the purpose of the file. The more Downwards the more details we got.

## 7. Line Length
-----------------
Limit lines to a maximum of 80 characters to avoid horizontal scrolling and improve readability. The file long should match the following hashes.
################################################################################

## 8. Blank Lines
-----------------
Use blank lines to separate logical sections of code, making it easier to navigate and understand.


## 9. Commenting
----------------
Write comments that explain "why" something is done, not "what" is done, as the code itself should be self-explanatory.
Avoiding copies comments, Instead refer to a created readme file.

## 10. Naming Conventions
-------------------------
Use meaningful names for variables, functions, and classes to convey their purpose clearly. 
Each file should have a clear and descriptive name.
follow the following rules:
- file name: ```my_program.py```
- class name: ```MyClass``` | ```PascalCase```
- function name: ```my_function```
- variable name: ```my_variable```

## 11. Function Length
---------------------
Keep functions small and focused on a single task. A good rule of thumb is to keep functions under 20 lines. Each function should have a single responsibility.


## 12. Avoid Deep Nesting
-------------------------
Limit the depth of nested structures to improve readability and maintainability. either use new line with indentation.



*Clean code Page 92*