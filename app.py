from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_anomalies', methods=['POST'])
def detect_anomalies():
    file = request.files['data_file']

    data = pd.read_csv(file)

    selected_features = ['speed', 'temperature', 'vibration']

    model = IsolationForest(contamination=0.05)
    model.fit(data[selected_features])

    predictions = model.predict(data[selected_features])
    anomalies = data[predictions == -1]

    return render_template('results.html', anomalies=anomalies)

if __name__ == '__main__':
    app.run(debug=True)