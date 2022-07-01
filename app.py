import csv
from flask import Flask, render_template,request,redirect,url_for
import prediction
#import mySQLdb

app = Flask(__name__)
# #conn = MySQLdb.connect(host='localhost',user='root',password='',db='disease_database')

with open('Database/Testing.csv', newline='') as f:
        reader = csv.reader(f)
        symptoms = next(reader)
        symptoms = symptoms[:len(symptoms)-1]
        
@app.route('/')
def index():
        return render_template('index.html')

@app.route('/predictdisease')
def predictdisease():
        return render_template('predictdisease.html')

@app.route('/disease_predict', methods=["GET", "POST"])
def disease_predict():
    selected_symptoms = []
    if(request.form['Symptom1']!="") and (request.form['Symptom1'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom1'])
    if(request.form['Symptom2']!="") and (request.form['Symptom2'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom2'])
    if(request.form['Symptom3']!="") and (request.form['Symptom3'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom3'])
    if(request.form['Symptom4']!="") and (request.form['Symptom4'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom4'])
    if(request.form['Symptom5']!="") and (request.form['Symptom5'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom5'])

    accuracy_val = prediction.accuracy_val()
    diseases = prediction.dosomething(selected_symptoms)
    fetched_data = diseases[0]
    fetched_data_list = fetched_data.split(":")
    disease = fetched_data_list[0]

    if len(fetched_data_list) == 2:
        cure = fetched_data_list[1]
    else:
        cure = ""
    return render_template('disease_predict.html',cure=cure,disease=disease,symptoms=symptoms,accuracy_val=accuracy_val)

@app.route('/blog1')
def blog1():
        return render_template('blog1.html')

@app.route('/blog2')
def blog2():
        return render_template('blog2.html')

@app.route('/blog3')
def blog3():
        return render_template('blog3.html')

@app.route('/blogA1')
def blogA1():
        return render_template('blogA1.html')

@app.route('/blogA2')
def blogA2():
        return render_template('blogA2.html')

@app.route('/blogA3')
def blogA3():
        return render_template('blogA3.html')        

if __name__ == '__main__':
    app.run(debug=True)