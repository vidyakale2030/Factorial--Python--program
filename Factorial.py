class FactorialSeries:
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.factorial = 1

    def __iter__(self):
        
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        if self.current == 0 or self.current == 1:
            self.factorial = 1
        else:
            self.factorial *= self.current
        result = self.factorial
        self.current += 1
        return result