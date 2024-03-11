class Money:

    def __init__(self, amount , currency):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            raise RuntimeError("Mismatched currencies!")
        
    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        else:
            raise RuntimeError("Mismatched currencies!")

    def __mul__(self, value):
        if isinstance(value, (int, float)):
            return Money(self.amount * value, self.currency)
        else:
            RuntimeError("Value is not a int or float")