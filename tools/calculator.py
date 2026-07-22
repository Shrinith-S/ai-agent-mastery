class CalculatorTool:
    
    def add(self, a , b ) -> float:
        return a + b

    def substract(self, a, b) -> float:
        return a - b

    def multiply(self, a , b) -> float:
        return a * b
    
    def divide(self, a , b) -> float:
        if b == 0:
            raise ValueError("Cannot be divide by zero")
        
        return a / b


    