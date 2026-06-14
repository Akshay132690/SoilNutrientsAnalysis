# SoilNutrientAnalysis

🌿 NutrientNavigator
NutrientNavigator is a web application designed to help farmers and gardeners optimize crop yields and promote healthier soil. By providing personalized fertilizer recommendations based on detailed soil analysis, it addresses the critical challenge of efficient fertilizer management.

<p align="center">
  <img src="/Screenshot 2025-04-01 163140.png" width="900">
</p>

📌 Key Features
✅ Intuitive Input Interface
Users can enter essential soil data, including:

Temperature

Moisture

pH levels

Nutrient concentrations (Nitrogen, Phosphorous, Potassium, Carbon)

Soil type

Crop type

✅ Real-Time Data Processing
User input is sent to the backend for analysis and prediction, ensuring quick, tailored results.

✅ Personalized Fertilizer Recommendations
The core functionality delivers specific fertilizer recommendations tailored to the provided soil conditions.

✅ Visual Data Representation
Dynamic bar charts, pie charts, and line graphs provide clear insights into nutrient distribution and trends.

🛠️ Technical Details

🔹 Backend: Python Flask

Handles data processing, prediction, and API communication.

🔹 Frontend: HTML, CSS, JavaScript

Fully responsive and engaging user interface.

🔹 Data Visualization:

Uses base64-encoded image data returned from the backend.

Graphs generated with Matplotlib.

🔹 Machine Learning:

Leverages the CatBoost model for accurate fertilizer recommendation.

🎯 Purpose and Impact
This project empowers farmers and gardeners with data-driven insights, enabling them to make informed decisions about fertilizer use. By optimizing application, NutrientNavigator contributes to:

🔺 Increased crop yields
🔺 Reduced environmental impact through minimized fertilizer waste
🔺 Improved long-term soil health

📸 Demo
https://drive.google.com/file/d/1Eg6YQ39t7BfRWmgl4cRwM_RHGVI-M30p/view?usp=sharing

⚙️ How to Run
Prerequisites
Python 3

Flask

CatBoost

Matplotlib

HTML/CSS/JS (static files)

Steps
Clone the repository

Install Python dependencies:

nginx
Copy
Edit
pip install flask catboost matplotlib
Run the Flask server:

nginx
Copy
Edit
python app.py
Open index.html in a browser and interact with the interface.

📜 License
This project is open source and free to use under the MIT License.

👤 Author
Akshay Ingle
