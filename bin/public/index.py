from flask import Flask, render_template, request
# Applying logistic regression on the training set

from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
# Importing the dataset


df = pd.read_csv("data.csv")
heart_data = df

# all parameters an user can input
all_features = heart_data.columns
# all_features = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 'ejection_fraction', 'high_blood_pressure', 'platelets', 'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time', 'DEATH_EVENT']

def calculate_probability(age, anaemia, diabetes, high_blood_pressure, smoking, sex):
    
    # input_from_doc = {'age': 75, 'anaemia': 0, 'creatinine_phosphokinase': 582, 'diabetes': 0, 'ejection_fraction': 20, 'high_blood_pressure': 1, 'platelets': 265000, 'serum_creatinine': 1.9, 'serum_sodium': 130, 'sex': 1}
    input_form_person = {'age': age, 'anaemia': anaemia, 'diabetes': diabetes, 'high_blood_pressure': high_blood_pressure, 'smoking': smoking, 'sex': sex}
    # Features = ['age', 'anaemia', 'diabetes', 'high_blood_pressure', 'sex', 'smoking', 'DEATH_EVENT']
    Features = list(input_form_person.keys()) # we set features to train our model on by observing which ones a person has put in.

    df_person = pd.DataFrame(input_form_person, index=[0]) # create person df for obtaining our result later on a trained model.


    ## TODO:_ we receive a dict from frontend here, hardcoded template for now
    dict_received = {} 
    features_used = dict_received.keys() # we extract features user used here, we will train our model with these

    x = heart_data[Features] # select data with the features we have available data for
    y = heart_data["DEATH_EVENT"]
    x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=2)

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

        # print(len(y_perc))

    # print_rez() # print results of the model

    # Making Confusion Matrix and calculating accuracy score
    mylist = []
    from sklearn.metrics import confusion_matrix, accuracy_score
    cm = confusion_matrix(y_test, y_pred)
    ac = accuracy_score(y_test, y_pred) # for out view
    mylist.append(ac)
    print(cm)
    print(ac)
    # -----------------------------------------

    # printing the value of our person likelihood of dying
    DEATH = round(y_OUT[0][0], 3) # return this number to the user
    # We should also retunr the accuracy of our MODEL to predict (SUM) true positive and false negative.
    ACCURACY = ac
    
    return [DEATH, ACCURACY]
    

# input_from_doc = {'age': 75, 'anaemia': 0, 'creatinine_phosphokinase': 582, 'diabetes': 0, 'ejection_fraction': 20, 'high_blood_pressure': 1, 'platelets': 265000, 'serum_creatinine': 1.9, 'serum_sodium': 130, 'sex': 1}

# input_form_person = {'age': 75, 'anaemia': 0, 'diabetes': 0, 'high_blood_pressure': 1, 'smoking': 0, 'sex': 1}

# print("our person will die with prob: ", data[0], "and with model accuracy", data[1])

# TODO: pass/return the values it to the frontend
# Return tuple (OUT, ACCURACY)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
  
@app.route('/connect', methods=['POST', 'GET'])
def form():
    age = request.form.get("age")
    anaemia = request.form.get("anameia")
    if anaemia == None:
        anaemia = 0
    else:
        anaemia = 1
        
    diabetes = request.form.get("diabetes")
    if diabetes == None:
        diabetes = 0
    else:
        diabetes = 1
        
    high_blood_pressure = request.form.get("high_blood_pressure")
    if high_blood_pressure == None:
        high_blood_pressure = 0
    else:
        high_blood_pressure = 1
        
    smoking = request.form.get("smoking")
    if smoking == None:
        smoking = 0
    else:
        smoking = 1
        
    sex = request.form.get("sex")
    if sex == 'male':
        sex = 1
    else:
        sex = 0
        
    
    data = calculate_probability(age, anaemia, diabetes, high_blood_pressure, smoking, sex)
    
    return render_template('index.html', name=data[0])
