# Applying logistic regression on the training set

from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
# Importing the dataset


df = pd.read_csv("data.csv")
heart_data = df



print(heart_data[heart_data.DEATH_EVENT == 1].shape[0])

# all parameters an user can input
all_features = heart_data.columns
# all_features = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 'ejection_fraction', 'high_blood_pressure', 'platelets', 'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time', 'DEATH_EVENT']

# input_from_doc = {'age': 75, 'anaemia': 0, 'creatinine_phosphokinase': 582, 'diabetes': 0, 'ejection_fraction': 20, 'high_blood_pressure': 1, 'platelets': 265000, 'serum_creatinine': 1.9, 'serum_sodium': 130, 'sex': 1}
input_form_person = {'age': 40, 'anaemia': 0, 'diabetes': 1,  'high_blood_pressure': 0, 'smoking': 0, 'sex': 1}

# Features = ['age', 'anaemia', 'diabetes', 'high_blood_pressure', 'sex', 'smoking', 'DEATH_EVENT']
Features = list(input_form_person.keys()) # we set features to train our model on by observing which ones a person has put in.
print("Features:")
print(Features)

df_person = pd.DataFrame(input_form_person, index=[0]) # create person df for obtaining our result later on a trained model.


## TODO:_ we receive a dict from frontend here, hardcoded template for now
dict_received = {} 
features_used = dict_received.keys() # we extract features user used here, we will train our model with these

x = heart_data[Features] # select data with the features we have available data for
y = heart_data["DEATH_EVENT"]
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.1, random_state=2) 

classifier = LogisticRegression() # load model type
classifier.fit(x_train, y_train) # train our model

# Predicting the test set
y_pred = classifier.predict(x_test) # binary values, array, 0 - death, 1 - alive; we don't really need these anymore
y_perc = classifier.predict_proba(x_test) # percentage values


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

print("our person will die with prob: ", DEATH, "and with model accuracy", ACCURACY)

# TODO: pass/return the values it to the frontend
# Return tuple (OUT, ACCURACY)