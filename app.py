from flask import Flask, request, render_template
import numpy as np
import pickle
import listsML

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    message = "Welcome to my flask based web application ... !!!"
    return render_template("home.html", message = message)

count = 1
months_dict = {}
for month in listsML.monthsList: 
    months_dict[month] = count
    count +=1


@app.route('/getResponseLinearReg',methods=["GET","POST"])
def getResponseLinearReg():
    
    passenger_count = int(request.form['passenger_count'])
    month = request.form['month']
    month = months_dict[month]
    print("MONTH: ",month)
    date = int(request.form['date'])
    hour = int(request.form['hour'])
    distance = float(request.form['distance'])

    inputList = [passenger_count,month,date,hour,distance]
    with open('xgboost_nycfare.sav', 'rb') as file:
            pickle_model = pickle.load(file)
            y_pred_from_pkl = pickle_model.predict(np.array([inputList]))
           
    
  
    print(y_pred_from_pkl)
    return str(" $%.2f" % np.around(y_pred_from_pkl[0],decimals=2))

if __name__ == '__main__':
    app.run(debug=True)