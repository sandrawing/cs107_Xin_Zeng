import numpy as np


class Regression():
    def __init__(self):
        # your code
        self.params = {}

    def get_params(self):
        # your code
        return self.params

    def set_params(self, **kwargs):
        # your code
        for arg in kwargs:
            self.params[arg] = kwargs[arg]

    def fit(self, X, y):
        # your code
        raise NotImplementedError

    def predict(self, X):
        # your code
        y_hat = np.dot(X, self.params['coef']) + self.params['intercept']
        return y_hat

    def score(self, X, y):
        # your code
        SST = np.sum((y - np.mean(y))*(y - np.mean(y)))
        y_hat = self.predict(X)
        SSE = np.sum((y - y_hat)*(y - y_hat))
        r_square = 1 - SSE / SST
        return r_square


class LinearRegression(Regression):
    def fit(self, X, y):
        X = np.append(X, np.ones((X.shape[0], 1)), axis=1)
        beta = np.dot(np.linalg.pinv(np.dot(X.T, X)), np.dot(X.T, y))
        self.params['intercept'] = beta[-1]
        self.params['coef'] = beta[:-1]


class RidgeRegression(Regression):
    def fit(self, X, y):
        X = np.append(X, np.ones((X.shape[0], 1)), axis=1)
        gamma = self.params['alpha'] * np.identity(X.shape[1])
        beta = np.dot(np.linalg.pinv(np.dot(X.T, X) + np.dot(gamma.T, gamma)), np.dot(X.T, y))
        self.params['intercept'] = beta[-1]
        self.params['coef'] = beta[:-1]