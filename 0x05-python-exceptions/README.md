0x05. Python - Exceptions
 Foundations - Higher-level programming ― Python

 by Guillaume, CTO at Holberton school

 Ongoing project - started 01-08-2020, must end by 01-09-2020 (in about 14 hours) - you're done with 0% of tasks.

 QA review fully automated.

Resources
Read or watch:

Errors and Exceptions
Learn to Program 11 Static & Exception Handling (starting at minute 7)
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
What’s the difference between errors and exceptions
What are exceptions and how to use them
When do we need to use exceptions
How to correctly handle an exception
What’s the purpose of catching exceptions
How to raise a builtin exception
When do we need to implement a clean-up action after an exception
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.*)
All your files must be executable
The length of your files will be tested using wc

Tasks

0. Safe list printing mandatory
Write a function that prints x elements of a list.

Prototype: def safe_print_list(my_list=[], x=0):
my_list can contain any type (integer, string, etc.)
All elements must be printed on the same line followed by a new line.
x represents the number of elements to print
x can be bigger than the length of my_list
Returns the real number of elements printed
You have to use try: / except:
You are not allowed to import any module
You are not allowed to use len()

1. Safe printing of an integers list mandatory
Write a function that prints an integer with "{:d}".format().

Prototype: def safe_print_integer(value):
value can be any type (integer, string, etc.)
The integer should be printed followed by a new line
Returns True if value has been correctly printed (it means the value is an integer)
Otherwise, returns False
You have to use try: / except:
You have to use "{:d}".format() to print as integer
You are not allowed to import any module
You are not allowed to use type()