from sklearn import datasets
from sklearn.model_selection import train_test_split
import Regression as reg

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
                                                    dataset['target'],
                                                    test_size=0.2,
                                                    random_state=42)

alpha = 0.1
rdg_regress = reg.RidgeRegression()
rdg_regress.set_params(alpha=alpha)
models = [reg.LinearRegression(), rdg_regress]

model_scores = {}
model_params = {}

for model in models:
    model.fit(X_train, y_train)
    model_scores[model.__class__.__name__] = model.score(X_test, y_test)
    model_params[model.__class__.__name__] = model.get_params()
    print("The model is : {}. The R-square value in the test dataset is : {}.".format(model.__class__.__name__,
                                                                                      model.score(X_test, y_test)))

best_model = max(model_scores, key=model_scores.get)
print("The best model is : {} \nParameters are : \n{}".format(best_model, model_params[best_model]))