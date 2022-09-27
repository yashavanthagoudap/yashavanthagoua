        //programing language python
        def add(x,y):
        return x+y
        
        def subtract(x,y):
        return x-y
        
        def multiply(x,y):
        return x*y
        
        def divide(x,y):
        return x/y
        print("select operation.")
        print("1. Add")
        print("2.Subtract")
        print("3. multiple")
        print("4.divide")
        
        while True:
        choice= input("Enter choice(1/2/3/4):)
        
        if choice in('1','2','3','4'):
        num1=double(input("Enter first number:"))
        num2=double(input("Enter second number:"))
        
        if choice=='1':
        print(num1, "+" , num "=", add(num1,num2))
        
        if choice=='2':
        print(num1, "-" , num "=", subtract(num1,num2))
        
        if choice=='3':
        print(num1, "*" , num "=", multiply(num1,num2))
        
        if choice=='4':
        print(num1, "/" , num "=", divide(num1,num2))
        
        next_calculation = input("lets do next calculation? (yes/no):")
        if next_calculation=="no":
        break
        
        else: 
        print("Invalid Input")
        
