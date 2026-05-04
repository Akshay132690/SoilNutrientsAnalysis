from flask import Flask, request, jsonify
import pandas as pd
from catboost import CatBoostClassifier
from flask_cors import CORS
import numpy as np
import re
import matplotlib.pyplot as plt
import io
import base64
import matplotlib
matplotlib.use('Agg')
app = Flask(__name__)
CORS(app)

# Load the trained model
model = CatBoostClassifier()
model.load_model("fertilizer_recommendation_model.cbm")

# Load the dataset for remarks
df = pd.read_csv("fertilizer_recommendation_dataset.csv")
df["Fertilizer"] = df["Fertilizer"].astype(str)

def generate_nutrient_plots(data):
    nutrients = ['Nitrogen', 'Phosphorous', 'Potassium', 'Carbon']
    values = [data['Nitrogen'], data['Phosphorous'], data['Potassium'], data['Carbon']]

    # Bar Chart
    plt.figure(figsize=(8, 6))
    plt.bar(nutrients, values)
    plt.xlabel('Nutrients')
    plt.ylabel('Values')
    plt.title('Soil Nutrient Levels (Bar Chart)')
    bar_img = io.BytesIO()
    plt.savefig(bar_img, format='png')
    bar_img.seek(0)
    plt.close()
    bar_img_base64 = base64.b64encode(bar_img.getvalue()).decode('utf-8')

    # Pie Chart
    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=nutrients, autopct='%1.1f%%')
    plt.title('Soil Nutrient Distribution (Pie Chart)')
    pie_img = io.BytesIO()
    plt.savefig(pie_img, format='png')
    pie_img.seek(0)
    plt.close()
    pie_img_base64 = base64.b64encode(pie_img.getvalue()).decode('utf-8')

    # Line Chart
    plt.figure(figsize=(8, 6))
    plt.plot(nutrients, values, marker='o')
    plt.xlabel('Nutrients')
    plt.ylabel('Values')
    plt.title('Soil Nutrient Trends (Line Chart)')
    line_img = io.BytesIO()
    plt.savefig(line_img, format='png')
    line_img.seek(0)
    plt.close()
    line_img_base64 = base64.b64encode(line_img.getvalue()).decode('utf-8')

    return bar_img_base64, pie_img_base64, line_img_base64

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received Data:", data)

        sample_data = pd.DataFrame([{
            'Temperature': data['Temperature'],
            'Moisture': data['Moisture'],
            'Rainfall': data['Rainfall'],
            'PH': data['PH'],
            'Nitrogen': data['Nitrogen'],
            'Phosphorous': data['Phosphorous'],
            'Potassium': data['Potassium'],
            'Carbon': data['Carbon'],
            'Soil': str(data['Soil']),
            'Crop': str(data['Crop'])
        }])

        categorical_cols = ['Soil', 'Crop']
        sample_data[categorical_cols] = sample_data[categorical_cols].astype(str)

        prediction = model.predict(sample_data)
        predicted_fertilizer = prediction[0]

        # Ensure it's a scalar value, not an array
        if isinstance(predicted_fertilizer, (list, np.ndarray)):
            predicted_fertilizer = predicted_fertilizer[0]

        predicted_fertilizer = re.sub(r'\s+', ' ', str(predicted_fertilizer).strip().lower())

        # Convert dataset column to lowercase for consistent matching
        df["Fertilizer"] = df["Fertilizer"].apply(lambda x: re.sub(r'\s+', ' ', str(x).strip().lower()))

        # Fetch the corresponding remark
        remark_row = df[df["Fertilizer"] == predicted_fertilizer]

        if not remark_row.empty:
            remark = remark_row["Remark"].values[0]
        else:
            remark = "No remark found."

        bar_plot, pie_plot, line_plot = generate_nutrient_plots(data)

        return jsonify({
            "Recommended Fertilizer": predicted_fertilizer,
            "Remark": remark,
            "BarPlot": bar_plot,
            "PiePlot": pie_plot,
            "LinePlot": line_plot
        })

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500
@app.route('/')
def home():
    return "Flask API is running 🚀"
if __name__ == '__main__':
    app.run(debug=True)