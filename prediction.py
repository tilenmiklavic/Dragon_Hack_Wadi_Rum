import pandas as pd
import numpy as np # linear algebra
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import os

df = pd.read_csv("data.csv")

# print(df)

features = ['age', 'anaemia', 'diabetes', 'high_blood_pressure', 'sex', 'smoking']

target = 'DEATH_EVENT'

x = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(x, y)

# Train Decision Tree Classifer
dtree = dtree.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = dtree.predict(X_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

print(dtree.predict([[78, 1, 1, 1, 1, 1]]))
print(dtree.predict_log_proba([[78, 1, 1, 1, 1, 1]]))

data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()
