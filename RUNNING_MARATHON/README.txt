
RUNNING MARATHON – Supervised ML Regression Project
===================================================

# 1) Overview
This project applies Supervised Machine Learning (Regression) to predict a runner’s marathon finishing time.  
The goal is to estimate **race time** or **pace** based on key training and personal indicators.

# 2) Problem Statement
**Target (y):** Race time in seconds (or pace in min/km).  
**Type:** Regression (Supervised ML).

# 3) Dataset
*Minimal required features:*
- `age` – runner’s age  
- `sex` – gender  
- `weekly_mileage_km` – weekly mileage  
- `longest_run_km` – longest training run  
- `previous_best_time_sec` – previous best race time  
- **Target:** `race_time_sec`

# 4) Project Structure
```
marathon-regression/
├─ data/               # raw and processed data
├─ notebooks/          # EDA and modeling Jupyter notebooks
├─ src/                # source code (train, evaluate, infer)
├─ models/             # saved models
├─ requirements.txt
└─ README.txt
```

# 5) Setup
```bash
conda create -n marathon-ml python=3.11 -y
conda activate marathon-ml
pip install -r requirements.txt
```

# 6) How to Run
```bash
# Data preparation
python -m src.data_prep --input data/raw/marathon.csv --output data/processed/train.csv

# Train model
python -m src.train --train data/processed/train.csv --model_dir models/

# Evaluate
python -m src.evaluate --val data/processed/train.csv --model_dir models/

# Inference (new runner)
python -m src.infer --model models/best_model.pkl --json samples/new_athlete.json
```

# 7) Models
- Linear Regression  
- Random Forest Regressor  
- XGBoost Regressor  

# 8) Evaluation Metrics
- MAE (average error in seconds)  
- RMSE  
- R²  

# 9) Results
- Real vs. Predicted plots  
- Feature importance analysis  

# 10) License
MIT License  
Author: Rasulbek (Data Science) – 2025
