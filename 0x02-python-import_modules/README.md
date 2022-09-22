# IMPORTING MODULES IN PYTHON

## WHAT IS A MOUULE?
---
A ***Module*** is a python file containing python definitions and statements. This files are used in an interactive instance of the interpreter. Definitions from a module can be imported into other modules or into the main module that you have access to in a script.

## IMPORTING A MODULE

To import a module, use the ***import*** statement.

There are various ways of using the import statement. If, for example, we have a file 'fibo.py', containing two functions 'fib()' and 'fib2()', and we want to import it for use in another file, we can say:
1. import fibo

This will not add the names of the functions defined in fibo directly to the current namespace. It only adds the module name fibo there. Uding the module name you can access the functions like so:
1. fibo.fib(100)
2. fibo,fib2(40)
