#-----------------------------------------------------------------------------
def function1():
    print('---------')
    print(f"function 1 - start")
    try:
        result = 10/0
    except ZeroDivisionError as e:
        print(f"Custom Error Handler: {e}")

    print(f"function 1 - end")
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def function2():
    print('---------')
    print(f"function 2 - start")
    try:
        result = 10/0
    except ZeroDivisionError as e:
        print(f"Custom Error Handler (ZeroDivisionError): {e}")
    except Exception as e:
        print(f"Custom Error Handler (Exception): {e}")
    print(f"function 2 - end")
#-----------------------------------------------------------------------------    
#-----------------------------------------------------------------------------
def function3():
    print('---------')
    print(f"function 3 - start")
    try:
        result = 10/0
    except Exception as e:
        print(f"Custom Error Handler (Exception): {e}")        
    except ZeroDivisionError as e:
        print(f"Custom Error Handler (ZeroDivisionError): {e}")

    print(f"function 3 - end")
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def function4(input = 0):
    print('---------')
    print(f"function 4 - start")
    print(f"function 4 input: {input}")
    try:
        result = 10/input
    except Exception as e:
        print(f"Custom Error Handler (Exception): {e}")        
    else:
        print(f"No error occurred. Result: {result}")

    print(f"function 4 - end")
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def function5(input = 0):
    print('---------')
    print(f"function 5 - start")
    print(f"function 5 input: {input}")
    try:
        result = 10/input
    except Exception as e:
        print(f"Custom Error Handler (Exception): {e}")        
    else:
        print(f"No error occurred. Result: {result}")
    finally:
        print(f"Finally block executed")

    print(f"function 5 - end")
#-----------------------------------------------------------------------------    

function1()
function2()
function3()
function4(0)
function4(2)
function5(0)
function5(2)