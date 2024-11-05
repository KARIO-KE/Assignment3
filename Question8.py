class Calculator:
    count = 0
    @staticmethod
    def add(num1, num2):
        Calculator.count += 1
        return num1 + num2
print("Sum of 5 and 3:", Calculator.add(5, 3))
print("Sum of 10 and 20:", Calculator.add(10, 20))
print("add() method has been called", Calculator.count, "times.")
