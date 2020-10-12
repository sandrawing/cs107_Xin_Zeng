from sklearn import datasets
from sklearn.model_selection import train_test_split
import Regression as reg
from matplotlib import pyplot as plt
import numpy as np


dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
                                                    dataset['target'],
                                                    test_size=0.2,
                                                    random_state=42)
num_alphas = 100
# calculate the R^2 scores for RidgeRegression model
ridge_model = reg.RidgeRegression()
ridge_scores = []
alphas = []
for interval in np.linspace(-2, 1, num_alphas):
    alpha = pow(10, interval)
    alphas.append(alpha)
    ridge_model.set_params(alpha=alpha)
    ridge_model.fit(X_train, y_train)
    ridge_scores.append(ridge_model.score(X_test, y_test))

# calculate the R^2 scores for LinearRegression model
ols_model = reg.LinearRegression()
ols_model.fit(X_train, y_train)
ols_score = ols_model.score(X_test, y_test)
ols_scores = [ols_score] * num_alphas

plt.figure()
plt.plot(alphas, ols_scores)
plt.plot(alphas, ridge_scores)
plt.xlabel('$\\alpha$')
plt.ylabel('$R^2$')
plt.legend(['Linear Regression', 'Ridge Regression'])
plt.title('Linear and Ridge Regression performance for various values of $\\alpha$')
plt.savefig('P2F.png')
print("Image saved.")