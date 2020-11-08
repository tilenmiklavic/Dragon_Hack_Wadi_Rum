# Applying logistic regression on the training set
import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
# Importing the dataset


df = pd.read_csv("data.csv")
heart_data = df

# number of dead people in dataset
print(heart_data[heart_data.DEATH_EVENT == 1].shape[0])

# all parameters an user can input
all_features = heart_data.columns
# all_features = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 'ejection_fraction', 'high_blood_pressure',
# 'platelets', 'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time', 'DEATH_EVENT']


creatinine_phosphokinase_mean = df["creatinine_phosphokinase"].mean()
ejection_fraction_mean = df["ejection_fraction"].mean()
platelets_mean = df["platelets"].mean()
serum_creatinine_mean = df["serum_creatinine"].mean()
serum_sodium_mean = df["serum_sodium"].mean()
time_mean = df["time"].mean()
# we wont be using time feature

print("creatinine_phosphokinase_mean: ", creatinine_phosphokinase_mean)


# input_from_doc = {'age': 75, 'anaemia': 0, 'creatinine_phosphokinase': 582, 'diabetes': 0, 'ejection_fraction': 20, 'high_blood_pressure': 1, 'platelets': 265000, 'serum_creatinine': 1.9, 'serum_sodium': 130, 'sex': 1}
# input_form_person = {'age': 40, 'anaemia': 0, 'diabetes': 1,  'high_blood_pressure': 0, 'sex': 1, 'smoking': 0}

dead_man = {'age': 75, 'anaemia': 0, 'diabetes': 0,  'high_blood_pressure': 1, 'sex': 1, 'smoking': 0}
alive_man = {'age': 49, 'anaemia': 1, 'diabetes': 0,  'high_blood_pressure': 1, 'sex': 0, 'smoking': 0}
ALIVE = True
if ALIVE:
    input_form_person = alive_man
else:
    input_form_person = dead_man
append_data = {'creatinine_phosphokinase': creatinine_phosphokinase_mean, 'ejection_fraction': ejection_fraction_mean, 'platelets': platelets_mean, 'serum_creatinine': serum_creatinine_mean, 'serum_sodium': serum_sodium_mean, 'time': time_mean}   

# append data if missing, but averages so it doesn't affect the result
for k,v in append_data.items():
    if k not in input_form_person.keys():
        input_form_person[k] = round(v,5)
print("input_form_person:", input_form_person)

# Features = ['age', 'anaemia', 'diabetes', 'high_blood_pressure', 'sex', 'smoking', 'DEATH_EVENT']

Features = list(input_form_person.keys()) # we set features to train our model on by observing which ones a person has put in.
print("Features:")
print(Features)

df_person = pd.DataFrame(input_form_person, index=[0]) # create person df for obtaining our result later on a trained model.


## TODO:_ we receive a dict from frontend here, hardcoded template for now
dict_received = {} 
features_used = dict_received.keys() # we extract features user used here, we will train our model with these

all_features = list(df.columns)

x = heart_data[Features] # select data with the features we have available data for
y = heart_data["DEATH_EVENT"]
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=2, shuffle=True) 

# Logistic regression documentation
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
classifier = LogisticRegression() # load model type

weights_custom = np.ones(239)
weights_custom[0] = 30
weights_custom = weights_custom / sum(weights_custom)

# clf = classifier.fit(x_train, y_train, sample_weight=weights_custom) # train our model with biased weights
clf = classifier.fit(x_train, y_train) # train our model


# Predicting the test set
y_pred = classifier.predict(x_test) # binary values, array, 0 - death, 1 - alive; we don't really need these anymore
y_perc = classifier.predict_proba(x_test) # percentage values

 # ----------------------------- 
weights = classifier.coef_
abs_weights = np.abs(weights)

# print(abs_weights)


# input the df rom a person to a trained model and get the result:
y_OUT = classifier.predict_proba(df_person)

def print_rez():

    print("Percent , class")
    # array of 2 elements means  [death, live] in percentages
    # so if death % is > 0.5, then the person will die with that prob 
    for percent, class_pred in zip(y_perc, y_pred):
        if class_pred == 0: # death
            print("dead:", round(percent[0],2), "%")
        
        else: # alive
            print("alive:", round(percent[1],2), "%")

    print(len(y_perc))

# print_rez() # print results of the model

# Making Confusion Matrix and calculating accuracy score
mylist = []
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test, y_pred) # for out view
mylist.append(ac)
print(cm)


print(round(ac,3))
# -----------------------------------------


# printing the value of our person likelihood of dying
DEATH = round(y_OUT[0][0], 3) # return this number to the user
# We should also retunr the accuracy of our MODEL to predict (SUM) true positive and false negative.
ACCURACY = round(ac,3)

if ALIVE:
    print("Our person should LIVE")
else:
    print("Our person should DIE")

print("our person will die with prob: ", DEATH, "and with model accuracy", ACCURACY)

# TODO: pass/return the values it to the frontend
# Return tuple (OUT, ACCURACY)
