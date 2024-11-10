import numpy as np
import pandas as pd

from sklearn.naive_bayes import GaussianNB
# from webapp.db import db
# from webapp.calculation.models import UserDataSet

df = pd.read_csv("webapp/calculation/user_1.csv")

# print(df.to_numpy())
# print(df.iloc[:, 7].to_list())
# print(df.iloc[:, 2].to_list(), df.iloc[:, 3].to_list())

result = list([i, j] for i, j in zip(df.iloc[:, 2].to_list(), df.iloc[:, 3].to_list()))
result1 = list(df.iloc[:, 4].to_list())
print(result)
print(result1)

X = np.array(result)
Y = np.array(result1)

clf = GaussianNB()
clf.fit(X, Y)

print(clf.predict([[10, 7]]))
clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))
print(clf_pf.predict([[10, 5]]))
