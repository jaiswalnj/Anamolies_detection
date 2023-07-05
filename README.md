# Anomaly Detection Flask Application

This is a Flask web application that utilizes scikit-learn's IsolationForest algorithm for anomaly detection. It allows you to upload a CSV file, select relevant features, and detect anomalies in the data.

## Prerequisites

Python 3.7 or above
Flask<br>
scikit-learn<br>
pandas

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running the following command:

   *pip install -r requirements.txt*

## Usage

1. Run the Flask application by executing the following command:

  *python app.py*

2. Open a web browser and access the application at http://localhost:5000.

3. On the home page, click the "Choose File" button and select a CSV file containing the data you want to analyze.

4. Select the relevant features for anomaly detection. Modify the selected_features list in the detect_anomalies function to include the column names from your dataset that you want to use for anomaly detection.

5. Adjust the contamination parameter in the IsolationForest model initialization based on your desired threshold for identifying anomalies. Higher values indicate a higher tolerance for anomalies.

6. Click the "Detect Anomalies" button to process the uploaded file and detect anomalies.

7. The results page will display the detected anomalies from the uploaded data.

## Customization

HTML Templates: The application uses two HTML templates: index.html and results.html. Customize these templates to modify the appearance and layout of the web pages.

Error Handling: Consider adding additional error handling and validation for a more robust application. You can customize the error messages and behaviors in the Flask routes as needed.

## License

This project is licensed under the MIT License.
