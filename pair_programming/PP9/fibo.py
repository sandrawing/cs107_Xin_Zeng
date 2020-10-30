#!/usr/bin/env python3
#PP9
#group members: John Alling, Xin Zeng, Hanwen Zhang

class Fibonacci: 
    def __init__(self, n): 
        self.n = n

    def __iter__(self):
        return FibonacciIterator(self.n) # Returns an instance of the iterator

    def __repr__(self):
        return 'fibonacci(%s)' % reprlib.repr(self.n)


class FibonacciIterator: # has __next__ and __iter__
    def __init__(self, n): 
        self.term0 = 0 
        self.term1 = 1
        self.index = 0
        self.n = n

    def __next__(self):
        if self.index >= self.n:
            raise StopIteration()
        else:
            end_cond = 1 / (self.n - self.index) # iteration stops when n = index
            self.new = self.term0 + self.term1
            self.term0 = self.term1
            self.term1 = self.new
            self.index += 1
        return self.new
    
    def __iter__(self):
        return self


fib = Fibonacci(10)
print(list(iter(fib)))