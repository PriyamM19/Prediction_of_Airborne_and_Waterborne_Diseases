from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
import csv,numpy as np,pandas as pd
import os

data = pd.read_csv(os.path.join("Database", "Training.csv"))
df = pd.DataFrame(data)
cols = df.columns
cols = cols[:-1]
x = df[cols]
y = df['prognosis']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
hack_set = set()

# Naive Bayes
naive = GaussianNB()
naive.fit(x_train, y_train)
#hack_set.add(*map(str, naive.predict(x_test)))
print(f"Naive Bayes: {naive.predict(x_test)}")

y_pred = naive.predict(x_test)
accuracy_naive = accuracy_score(y_test, y_pred) * 100
print(f"Accuracy for Naive Bayes: {accuracy_naive}%")

# Decision Tree
dt = DecisionTreeClassifier()
clf_dt=dt.fit(x_train,y_train)
# print(f"Decision Tree: {dt.predict(x_test)}")

y_pred = dt.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy Decision Tree: {accuracy * 100}%")

# Random Forest
random = RandomForestClassifier()
random.fit(x_train, y_train)
#hack_set.add(*map(str, random.predict(x_test)))
# print(f"Random Forest: {random.predict(x_test)}")

y_pred = random.predict(x_test)
accuracy_random = accuracy_score(y_test, y_pred) * 100
print(f"Accuracy for Random Forest: {accuracy_random}%")

indices = [i for i in range(62)]
symptoms = df.columns.values[:-1]

dictionary = dict(zip(symptoms,indices))

def accuracy_val():
    return(accuracy_naive)

def dosomething(symptom):
    user_input_symptoms = symptom
    user_input_label = [0 for i in range(62)]
    for i in user_input_symptoms:
        idx = dictionary[i]
        user_input_label[idx] = 1

    user_input_label = np.array(user_input_label)
    user_input_label = user_input_label.reshape((-1,1)).transpose()
    return(naive.predict(user_input_label))