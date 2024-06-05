import pickle
from flask import Flask, render_template, request, redirect
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/prediction1')
def prediction1():
    return render_template('Crop.html')

@app.route('/prediction2')
def prediction2():
    return render_template('Fertilizer.html')    


@app.route('/form1', methods=["POST"])
def brain1():
    Nitrogen = float(request.form['Nitrogen'])
    Phosphorus = float(request.form['Phosphorus'])
    Potassium = float(request.form['Potassium'])
    Temperature = float(request.form['Temperature'])
    Humidity = float(request.form['Humidity'])
    Ph = float(request.form['ph'])
    Rainfall = float(request.form['Rainfall'])
     
    values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]
    
    if Ph>0 and Ph<=14 and Temperature < 100 and Humidity > 0:
        with open('crop_Recommendation.pkl', 'rb') as file:  
           Pickled_Model = pickle.load(file)
        arr = [values]
        acc = Pickled_Model.predict(arr) 
        return render_template('crop_prediction.html', prediction1=str(acc))       
    else:
        return "Sorry...  Error in entered values in the form Please check the values and fill it again"

@app.route('/form2', methods=["POST"])
def brain2():
    with open('croptype_dict.pkl', 'rb') as file:  
           Crop_Type = pickle.load(file)

    Temparature1 = float(request.form['Temparature'])
    Humidity1 = float(request.form['Humidity'])
    Moisture1 = float(request.form['Moisture'])
    Crop1 = request.form['Crop_Type']  # Assuming crop type is a string

    # Convert crop type string to numeric value
    if Crop1 in Crop_Type:
        crop_type = Crop_Type[Crop1]
    else:
        # Handle the case where crop type is not found in the dictionary
        crop_type = None  # or choose a default value, raise an error, etc.
    Nitrogen1 = float(request.form['Nitrogen'])
    Potassium1 = float(request.form['Potassium'])
    Phosphorous1 = float(request.form['Phosphorous'])
     
    values1 = [Temparature1, Humidity1, Moisture1, crop_type, Nitrogen1, Potassium1, Phosphorous1]
    
    with open('fert_Recommendation.pkl', 'rb') as file:  
           Pickled_Model = pickle.load(file)
    #with open('croptype_dict.pkl', 'rb') as file:  
     #      Pickled_Model1 = pickle.load(file)
    arr1 = [values1]
    acc1 = Pickled_Model.predict(arr1) 
    return render_template('fertilizer_prediction.html', prediction2=str(acc1))    
    


if __name__ == '__main__':
    app.run(debug=True, port="2000")















