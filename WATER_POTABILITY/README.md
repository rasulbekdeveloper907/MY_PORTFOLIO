# 💧 Water Potability Prediction  

A **Machine Learning** project that predicts whether water is **safe (potable) or unsafe** for drinking based on its **physicochemical properties** using **classification models**.  
This project demonstrates **data preprocessing, exploratory analysis, feature engineering, model training, and evaluation** with a focus on **public health applications**.  

---

## 📌 What is Water Potability?  

**Water potability** indicates if water is **safe for human consumption**.  
It depends on various **chemical, physical, and biological parameters**. In this project, prediction is based on physicochemical properties:  

- **pH** (acidity/alkalinity)  
- **Hardness** (mineral content)  
- **Solids (TDS)** (dissolved substances)  
- **Chloramines** (disinfectant level)  
- **Sulfate**  
- **Conductivity** (ion concentration)  
- **Organic Carbon**  
- **Trihalomethanes** (disinfection byproducts)  
- **Turbidity** (clarity of water)  

📊 The target variable:  

- **0 → Not Potable (unsafe)**  
- **1 → Potable (safe)**  

---

## 🎯 Project Objective  

To build a **classification model** that predicts **water potability** using chemical indicators, enabling:  

- 🏥 **Public health safety** monitoring  
- 🚰 **Water treatment optimization**  
- 🏭 **Environmental & industrial policy support**  

---

## 🔍 Approach & Workflow  

### 1️⃣ Data Loading & Cleaning  
- Load dataset: `water_potability.csv`  
- Handle missing values (imputation / removal).  

### 2️⃣ Exploratory Data Analysis (EDA)  
- Visualize feature distributions.  
- Check class imbalance (safe vs unsafe water).  
- Correlation heatmap to see key factors.  

### 3️⃣ Feature Selection & Engineering  
- Select physicochemical properties as features.  
- Normalize/scale features for ML models.  

### 4️⃣ Model Training  
- Train/Test split.  
- Classification models tested:  
  - **Logistic Regression**  
  - **Random Forest Classifier**  
  - **Gradient Boosting (XGBoost/LightGBM)**  

### 5️⃣ Model Evaluation  
Metrics used:  
- **Accuracy**  
- **Precision, Recall, F1-score**  
- **ROC-AUC Curve**  

📊 Visualization: **Confusion Matrix** + **ROC Curve** for performance check.  

---

## 📈 Results & Insights  

- **Best Model:** Random Forest / Gradient Boosting showed the highest accuracy.  
- **Important Features:** pH, Hardness, Solids, and Chloramines strongly influence potability.  
- **Class Imbalance Handling:** SMOTE or class weights improve fairness.  

---

## 🛠 Technologies Used  

- **Python**  
- **Pandas, NumPy** – Data Processing  
- **Matplotlib, Seaborn** – Visualization  
- **Scikit-learn** – Machine Learning  

---

## 📂 Repository Structure  

```
├── Water_Potability.ipynb      # Main Jupyter Notebook
├── water_potability.csv        # Dataset
├── README.md                   # Project Documentation
└── requirements.txt            # Dependencies
```  

---

## 🚀 Future Enhancements  

- ✅ Try **Deep Learning models (ANN, CNN)** for better performance  
- ✅ Deploy as a **Flask/Django Web App** for live predictions  
- ✅ Integrate **real-time water quality monitoring sensor data**  

---

## 📜 License  

This project is open-source and available under the **MIT License**.  

---

If you like this project, ⭐ **star the repository** to support further work!  
