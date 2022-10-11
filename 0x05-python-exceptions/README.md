# PYTHON EXCEPTIONS

There are two types of errors in Python:
1. Syntax Errors
2. Exceptions

Syntax errors are caused by errors in the syntactic presentation of python codes. This includes missing out a colon or parenthesis. 


Exceptions are thrown when the interpreter encounters a special type of error. This errors are handled by writing special programs which handle them using the ***try...except*** structure.


### the try statements work as follows
1. First, the try clause (the statements between the try and except) is executed
2. if no exception occurs, the except clause is not executed and the try satement is finished
3. if an exception occurs during the executionof the try clause, the other codes are skipped. Then if its type matches the exception named in the except keyword, the exccept clause if executed and the execution continues after the try and exccept block.
4. if an exception which does not matchthe excetion named in the  except clause, it is passed on to the outer try statements. if no handler is found, it is an unhandled exception. 


