import pandas as pd
import numpy as np # linear algebra
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import os

df = pd.read_csv("data.csv")

# print(df)

features = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
            'ejection_fraction', 'high_blood_pressure' ,
            'platelets', 'serum_creatinine', 'serum_sodium', 'sex',
            'smoking', 'time']

target = 'DEATH_EVENT'

x = df[features]
y = df[target]

dtree = DecisionTreeClassifier()
dtree = dtree.fit(x, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()
