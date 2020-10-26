# Toy AD Implementation
class AutoDiffToy():
    def __init__(self, val, der=1.0):
        self.val = val
        self.der = der

    def __add__(self, other):
        try:
            val = other.val + self.val
            der = other.der + self.der
        except AttributeError:
            val = other + self.val
            der = self.der
        return AutoDiffToy(val, der)

    def __mul__(self, other):
        try:
            der = self.der * other.val + self.val * other.der
            val = self.val * other.val
        except AttributeError:
            der = self.der * other
            val = self.val * other
        return AutoDiffToy(val, der)

    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)


if __name__ == '__main__':
    a = 2.0
    x = AutoDiffToy(a)

    alpha = 2.0
    beta = 3.0
    f_lst = [alpha * x + beta, x * alpha + beta, beta + alpha * x, beta + x * alpha]
    p_lst = ["f1 = alpha * x + beta", "f2 = x * alpha + beta",
             "f3 = beta + alpha * x", "f4 = beta + x * alpha"]
    print("alpha {}, beta {}, x value {}".format(alpha, beta, x.val))
    for i in range(len(f_lst)):
        f = f_lst[i]
        print(p_lst[i] + ", value {}, derivative {}.".format(f.val, f.der))
