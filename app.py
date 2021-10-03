from flask import Flask,render_template,request
import pickle
import numpy as np

app= Flask(__name__,template_folder="template")
model=pickle.load(open('weatpred.pkl','rb'))
print('model loaded')

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
  # if request.method == 'POST':
    print('proceed to prediction')
    Location =float(request.form['location'])
    MinTemp = float(request.form['mintemp'])
    MaxTemp = float(request.form['maxtemp'])
    rainfall = float(request.form['rainfall'])
    Evaporation = float(request.form['evaporation'])
    Sunshine = float(request.form['sunshine'])
    Windgustdir = request.form['windgustdir']
    Windgustspeed = float(request.form['windgustspeed'])
    Windir9am = request.form['winddir9am']
    Winddir3pm = request.form['winddir3pm']
    Windspeed9am = float(request.form['windspeed9am'])
    Windspeed3pm = float(request.form['windspeed3pm'])
    Humidity9am = float(request.form['humidity9am'])
    Humidity3pm = float(request.form['humidity3pm'])
    Pressure9am = float(request.form['pressure9am'])
    Pressure3pm = float(request.form['pressure3pm'])
    Cloud9am =float(request.form['cloud9am'])
    Cloud3pm = float(request.form['cloud3pm'])
    Temp9am = float(request.form['temp9am'])
    Temp3pm = float(request.form['temp3pm'])
    Raintoday = float(request.form['raintoday'])
    Year = float(request.form['year'])
    Month = float(request.form['month'])
    Day = float(request.form['day'])
    Season = request.form['season']
    # arr = np.array([[Location,MinTemp,MaxTemp,rainfall,Evaporation,Sunshine,Windgustdir,Windgustspeed,Windir9am,Winddir3pm,Windspeed9am,Windspeed3pm,
    #       Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,Temp9am,Temp3pm,Raintoday,Year,Month,Day,Season]])

    pred= model.predict([[Location,MinTemp,MaxTemp,rainfall,Evaporation,Sunshine,Windgustdir,Windgustspeed,Windir9am,Winddir3pm,Windspeed9am,Windspeed3pm,
          Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,Temp9am,Temp3pm,Raintoday,Year,Month,Day,Season]])
    # print(Location,MinTemp,MaxTemp,rainfall,Evaporation,Sunshine,Windgustdir,Windgustspeed,Windir9am,Winddir3pm,Windspeed9am,Windspeed3pm,
    #       Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,Temp9am,Temp3pm,Raintoday,Year,Month,Day,Season)

    print(pred[0])
    if pred[0] == 0:
       return render_template("after_sunny.html")
    else:
       return render_template("after_rainy.html")

    return render_template('after.html')

if __name__ == '__main__':
    app.run(debug=True)