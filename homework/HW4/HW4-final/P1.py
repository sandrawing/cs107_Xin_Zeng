import numpy as np
import matplotlib.pyplot as plt


# Part A: Write a Numerical Differentiation Closure
def numerical_diff(f, h):
    def wrapper(x):
        return (f(x + h) - f(x)) / h

    return wrapper


# Part B: Compare the Finite Difference to the True Derivative
x = np.linspace(0.2, 0.4, 100)
y_true = 1 / x
h1, h2, h3 = 1e-1, 1e-7, 1e-15
y_numerical_1 = numerical_diff(np.log, h1)(x)
y_numerical_2 = numerical_diff(np.log, h2)(x)
y_numerical_3 = numerical_diff(np.log, h3)(x)

plt.plot(x, y_true, 'cx--', label='True Derivative')
plt.plot(x, y_numerical_1, label='Estimated derivative h=1e-1')
plt.plot(x, y_numerical_2, label='Estimated derivative h=1e-7')
plt.plot(x, y_numerical_3, label='Estimated derivative h=1e-15')
plt.xlabel('x')
plt.ylabel('Derivative f\'(x)')
plt.legend()
plt.title("Comparison of numerically estimated derivatives to the analytic derivative", fontsize=10)

print('Answer to Q-a: \n\
1. The value 1e-7 of h most closely approximates the true derivative. \n\
2. When h is too small, there will be numerical instability problem. '
      'And we will encounter roundoff error. '
      'Since the floating point error is relative, and can essentially store 16 digits of accuracy. '
      'So let\'s say we choose h=1e-7. Then f(x + h) - f(x) is roughly the same in the first 7 digits, '
      'meaning that after the subtraction there is only 9 digits of accuracy, and then dividing by 1e-7 '
      'simply brings those 9 digits back up to the correct relative size.'
      'and approximation errors in the value of np.log are scaled significantly by the division operation.\n\
3. When h is too large, the approximation we get is not accurate. '
      'We could not get close to the real value of the derivative. '
      'The approximation is generally lower than the true value.')

print('\nAnswer to Q-b: \n\
The finite difference approach is nice because it is quick and easy. '
      'However, it suffers from accuracy and stability problems. '
      'On the other hand, symbolic derivatives can be evaluated to machine precision, but can be costly to evaluate. '
      'Automatic differentiation (AD) overcomes both of these deficiencies. It is less costly than symbolic '
      'differentiation while evaluating derivatives to machine precision. '
      'There are two modes of automatic differentiation: forward and reverse. '
      'Automatic differentiation calculates the value of a derivative with the help of the elementary rule set from '
      'symbolic differentiation. In order to overcome the swelling the symbolic expression is simplified at every stage. '
      'Simply by numerically evaluating with the results of the previous computations (or simply the input data). '
      'Hence, it does not provide an analytical expression for the derivative itself. '
      'Instead, it iteratively evaluates a gradient given data.')

plt.savefig('P1_fig.png')
plt.show()

