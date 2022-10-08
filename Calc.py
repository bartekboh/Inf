#Calculations
class Calculator:
    def add(a, b):
        x = a+b
        try:
            print(f"{a}+{b} is equal to {x}")
        finally:
            return x
    
    def sub(a, b):
        x = a-b
        try:
            print(f"{a}-{b} is equal to {x}")
        finally:
            return x
        
    def mult(a,b):
        x = a * b
        try:
            print(f"{a}*{b} is equal to {x}")
        finally:
            return x
    
    def div(a,b):
        x = a/b
        try:
            print(f"{a}/{b} is equal to {x}")
        finally:
            return x