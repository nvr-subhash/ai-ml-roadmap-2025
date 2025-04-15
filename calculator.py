print ("welcome to the Python Calculator")

operation = input("choose an operation( + , - , * , / ): ")

num1 = float(input("Enter number 1 : "))
num2 = float(input("Enter number 2 : "))

if operation == "+" :
    result = num1+num2
    print(f" The result of {num1} + {num2} is: {result}")
    
elif operation == "-" :
    result = num1-num2
    print(f" The result of {num1} - {num2} is: {result}")
    
elif operation == "*" :
    result = num1*num2
    print(f" The result of {num1} * {num2} is: {result}")
    
elif operation == "/" :
    if num2 != 0:
        result = num1/num2
        print(f" The result of {num1} / {num2} is: {result}")
    else:
        print("Error, cannot divided by 0")
        
else:
    print("Invalid operation, Choose an operation from ( + , - , * or /)")
        