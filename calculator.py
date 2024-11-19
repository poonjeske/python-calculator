class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        negative = (a < 0) ^ (b < 0)

        a = -a if a < 0 else a
        b = -b if b < 0 else b

        for _ in range(b):
            result = self.add(result, a)

        return -result if negative else result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("no result for Division by zero")
        negative = (a < 0) ^ (b < 0)

        a = -a if a < 0 else a
        b = -b if b < 0 else b

        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1

        return -result if negative else result

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("no result for modulo by zero.")
        negative = a < 0
        a = -a if a < 0 else a
        b = -b if b < 0 else b
        
        while a >= b:
            a = self.subtract(a, b)

        return -a if negative else a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(-10, 2))
    print("Example: modulo: ", calc.modulo(-10, 3))