from flask import Flask,request,render_template
import joblib
import pandas as pd
app = Flask(__name__)
with open(r"model1.pkl", 'rb') as file:
    model = joblib.load(file)
@app.route('/')
def rend_root():
    return render_template('index.html')

@app.route('/us')
def rend_us():
    return render_template('us.html')

@app.route('/predict',methods=['POST'])
def predict():
    airline = request.form['Airline'].strip().capitalize()
    airline_code = request.form['Flight'].strip().capitalize()
    source = request.form['SourceCity'].strip().capitalize()
    stops = request.form['Stops'].strip().capitalize()
    time = request.form['ArrivalTime'].strip().capitalize()
    destination = request.form['DestinationCity'].strip().capitalize()
    class_type = request.form['Class'].strip().capitalize()
    duration = float(request.form['Duration'])
    days_left = int(request.form['DaysLeft'])

    columns = ["airline", "flight", "source_city", "stops", "arrival_time", "destination_city", "class", "duration", "days_left"]
    data = pd.DataFrame([[airline, airline_code, source, stops, time, destination, class_type, duration, days_left]],columns=columns)
    output=model.predict(data)[0]

    return render_template('index.html',predict_text=f"prediction is {round(output,2)} $")





if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

