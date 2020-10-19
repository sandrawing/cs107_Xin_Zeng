def my_pow(x,r):
    return (x**r, r*x**(r-1))

#Testing with x=3 r=4
if __name__ == "__main__":
    test=my_pow(3,4)
    print('test=',test)