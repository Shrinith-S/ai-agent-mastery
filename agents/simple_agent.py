from tools.calculator import CalculatorTool


class SimpleAgent:

    def __init__(self):
        self.calculator = CalculatorTool()

    def run(self, user_input):

        user_input = user_input.lower()

        if "add" in user_input:
            result = self.calculator.add(10,15)
            return f"The sum is {result}"

        return "Sorry, I don't know how to do that"