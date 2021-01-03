import sqlite3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer


def save_to_database(model_id, model_desc, db, model, X_train, X_test, y_train, y_test):
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    cursor = db.cursor()

    model_params = model.get_params()
    for param_name, value in model_params.items():
        model_params_to_insert = (int(model_id), model_desc, param_name, value)
        cursor.execute('''INSERT INTO model_params 
                  (id, desc, param_name, value)
                  VALUES (?, ?, ?, ?)''', model_params_to_insert)

    model_coef = model.coef_[0]
    for i, val in enumerate(model_coef):
        feature_name = X_train.columns[i]
        model_coef_to_insert = (int(model_id), model_desc, feature_name, val)
        cursor.execute('''INSERT INTO model_coefs 
                  (id, desc, feature_name, value)
                  VALUES (?, ?, ?, ?)''', model_coef_to_insert)
    intercept_to_insert = (int(model_id), model_desc, 'intercept', model.intercept_[0])
    cursor.execute('''INSERT INTO model_coefs 
          (id, desc, feature_name, value)
          VALUES (?, ?, ?, ?)''', intercept_to_insert)

    model_results_to_insert = (int(model_id), model_desc, train_score, test_score)
    cursor.execute('''INSERT INTO model_results 
          (id, desc, train_score, test_score)
          VALUES (?, ?, ?, ?)''', model_results_to_insert)

    db.commit()


# Part A: Database schema
db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")

cursor.execute('''CREATE TABLE model_params (
               id INTEGER, 
               desc TEXT, 
               param_name TEXT, 
               value FLOAT)''')
db.commit()

cursor.execute('''CREATE TABLE model_coefs (
               id INTEGER, 
               desc TEXT, 
               feature_name TEXT, 
               value FLOAT)''')
db.commit()

cursor.execute('''CREATE TABLE model_results (
               id INTEGER, 
               desc TEXT, 
               train_score FLOAT, 
               test_score FLOAT)''')
db.commit()


# Part B: Inserting records
# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

# Fit model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)
save_to_database(1, "Baseline model", db, baseline_model, X_train, X_test, y_train, y_test)

# Reduced logistic regression model
feature_cols = ['mean radius',
                'texture error',
                'worst radius',
                'worst compactness',
                'worst concavity']

X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]

reduced_model = LogisticRegression(solver='liblinear')
reduced_model.fit(X_train_reduced, y_train)
save_to_database(2, "Reduced model", db, reduced_model, X_train_reduced, X_test_reduced, y_train, y_test)

# Logistic regression model with L1 penalty
penalized_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
penalized_model.fit(X_train, y_train)
save_to_database(3, "L1 penalty model", db, penalized_model, X_train, X_test, y_train, y_test)


# Part C: Database queries
cursor = db.cursor()
query = '''SELECT id, test_score FROM model_results WHERE test_score = (SELECT MAX(test_score) FROM model_results) '''
model_detail = cursor.execute(query).fetchall()
best_model_id = model_detail[0][0]
best_val_score = model_detail[0][1]
print("Best model id: {}".format(best_model_id))
print("Best validation score: {}".format(best_val_score))
print()

query = '''SELECT feature_name, value FROM model_coefs WHERE id == {}'''.format(best_model_id)
feature_detail = cursor.execute(query).fetchall()
for row in feature_detail:
    print("{}: {}".format(row[0], row[1]))
print()

test_model = LogisticRegression(solver='liblinear')
test_model.fit(X_train, y_train)

# Manually change fit parameters
best_coef = [row[1] for row in feature_detail][:-1]
best_intercept = feature_detail[-1][1]
test_model.coef_ = np.array([best_coef])
test_model.intercept_ = np.array([best_intercept])

test_score = test_model.score(X_test, y_test)
print(f'Reproduced best validation score: {test_score}')

db.close()
