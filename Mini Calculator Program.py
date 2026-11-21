operator = input("Enter an operator(+ - */")
num1 = float(input("Enter your first number :"))
num2 = float(input("Enter your second numbr :"))
             
if operator == "+" :
        result = num1 + num2 
        print("Your result is {result} ")

elif operator == "-" : 
        result = num1 - num2 
        print("Your result is {result}")

elif operator == "*" :
        result = num1 * num2 
        print("Ypur result is {result}")

elif operator == "/" :
        result = num1/num2
        print("Your result is {result}")