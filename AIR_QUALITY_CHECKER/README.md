# 🌍 Air Quality Index (AQI) Prediction  

A **Machine Learning** project that predicts **Air Quality Index (AQI)** values based on real-world pollutant levels using **regression models**.  
This project demonstrates **data preprocessing, exploratory analysis, feature engineering, model training, and evaluation** with a focus on environmental health applications.  

---

## 📌 What is AQI?  

The **Air Quality Index (AQI)** is a standardized indicator that reports the air quality of a specific area.  
It is calculated using the concentrations of major pollutants:  

- **PM2.5** (Particulate Matter ≤ 2.5 µm)  
- **PM10** (Particulate Matter ≤ 10 µm)  
- **NO₂** (Nitrogen Dioxide)  
- **SO₂** (Sulfur Dioxide)  
- **CO** (Carbon Monoxide)  
- **O₃** (Ozone)  

AQI values indicate the potential health impact of air pollution:  

| AQI Category                  | Range    |
|-------------------------------|----------|
| ✅ Good                        | 0 – 50   |
| 🟡 Moderate                    | 51 – 100 |
| 🟠 Unhealthy                    | 101 – 150|
| 🔴 Unhealthy for Sensitive     | 151 – 200|
| ☠️ Hazardous                   | 201+     |

---

## 🎯 Project Objective  

To build a **regression model** capable of accurately predicting AQI values from pollutant measurements, enabling:  

- 📢 **Early warnings** for public health  
- 🌱 **Environmental monitoring**  
- 🏛 **Government & industrial policy planning**  

---

## 🔍 Approach & Workflow  

### 1️⃣ Data Loading & Cleaning  
- Load dataset: `AirQualityUCI.csv`  
- Handle missing values and select relevant pollutant features.  

### 2️⃣ Exploratory Data Analysis (EDA)  
- Visualize pollutant distributions & AQI range.  
- Compute **correlation matrix** to identify key predictors.  

### 3️⃣ Feature Selection & Engineering  
- Select pollutant variables as model features.  
- Optional: Create derived features (e.g., pollutant ratios).  

### 4️⃣ Model Training  
- Train/Test split.  
- Model: **Random Forest Regressor**.  

### 5️⃣ Model Evaluation  
Metrics used:  
- **Root Mean Squared Error (RMSE)**  
- **Mean Absolute Error (MAE)**  
- **R² Score** (explained variance)  

📊 Visualization: **Actual vs Predicted AQI** scatter plot for performance check.  

---

## 📈 Results & Insights  

- **R² Score:** Shows how much of AQI variance is explained by pollutants.  
- **Lower RMSE & MAE:** Indicate stronger prediction accuracy.  
- **EDA Observations:** PM2.5 and PM10 have the strongest correlation with AQI.  

---

## 🛠 Technologies Used  

- **Python**  
- **Pandas, NumPy** – Data Processing  
- **Matplotlib, Seaborn** – Visualization  
- **Scikit-learn** – Machine Learning  

---

## 📂 Repository Structure  

```
├── Air_Quality_Index.ipynb     # Main Jupyter Notebook
├── AirQualityUCI.csv           # Dataset
├── README.md                   # Project Documentation
└── requirements.txt            # Dependencies
```

---

## 🚀 Future Enhancements  

- ✅ Try **Gradient Boosting** models (XGBoost, LightGBM, CatBoost)  
- ✅ Deploy as a **Flask/Django Web App** for live AQI prediction  
- ✅ Integrate **real-time data** from APIs like OpenAQ  

---

## 📜 License  

This project is open-source and available under the **MIT License**.  

---

If you like this project, ⭐ **star the repository** to support further work!  
