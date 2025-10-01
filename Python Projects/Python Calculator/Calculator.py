# Simple Calcualtor 

class Calculator():
    def __init__(self,number,other,operation):
        self.number = number
        self.other = other
        self.operation = operation
    def mult(self,number,other):
        self.number = number * other
        self.operation = " * "
        return self
    def div(self,number,other):
        self.number = number / other
        self.operation = " / "
        return self
    def add(self,number,other):
        self.number = number + other
        self.operation = " + "
        return self
    def sub(self,number,other):
        self.number = number - other
        self.operation = " - "
        return self

# Instantiate the object for calc
Calc = Calculator(0,0," ")


#While Loop Calc Function
while(1):
    # Welcome Message
    print("Welcome to Simple Calculator, Press 1 for Add, Press 2 for Subtract, Press 3 for Multiply, Press 4 for Division, Press 5 to End\n")

    #Get user operation
    user_Input = int(input("Enter Operation: "))
    operation = " "
    #User Error Check

    #Assign Nums
    if(user_Input != 5):
         num1 = int(input("\n Enter Number 1: "))
         num2 = int(input("\n Enter Number 2: "))

    #Switch Case Calculator
    def switch_Calc(user_Input):
        match user_Input:
            case 1:                
                return Calc.add(num1,num2)
            case 2:              
                return Calc.sub(num1,num2)
            case 3:              
                return Calc.mult(num1,num2)
            case 4:              
                return Calc.div(num1,num2)
            case 5:
                exit()
            case _:
                return "Invalid Option"
    #Print Output
    result = switch_Calc(user_Input).number
    print(num1, Calc.operation , num2, " = ", result , "\n")
    
    #Reset calcultor
    Calc.number = 0
     

    

    
    
