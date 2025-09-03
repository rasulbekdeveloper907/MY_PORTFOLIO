# 🏃 TWO CENTURIES OF UM RACES – REGRESSION PROJECT

## 📖 Loyiha Maqsadi
Ushbu loyiha insonning yugurish qobiliyatini (qancha km yugura olishini) bashorat qilish uchun **Machine Learning Regression** modelini yaratishga qaratilgan.  

Dataset Kaggle’dagi **"Two Centuries of UM Races"** dan olingan bo‘lib, 1798–2022 yillar oralig‘ida marafon va ultra-marafon musobaqalari haqidagi ma’lumotlarni o‘z ichiga oladi.

---

## ⚙️ Texnologiyalar
- Python 3.10+
- **pandas**, **numpy** – ma’lumotlarni qayta ishlash
- **scikit-learn** – ML modellari (Linear Regression, Ridge, RandomForest, HistGradientBoosting)
- **matplotlib** – vizualizatsiya
- **joblib** – modelni saqlash

---

## 📂 Loyiha Tuzilishi
```
UM_Races_Regression/
│
├── um_regression_pipeline.py    # Asosiy ML pipeline skripti
├── UM_RACES.csv                 # Dataset (Kaggle’dan yuklab olingan)
├── README.md                    # Loyihaning hujjati
│
├── um_best_model.joblib         # Eng yaxshi model (pipeline bilan)
├── um_metrics_report.json       # CV natijalari (RMSE/MAE/R2)
├── um_feature_importance.png    # Top featur’lar grafikasi
├── um_used_columns.json         # Qaysi ustunlar ishlatilgani haqida ma’lumot
```

---

## 🚀 Qanday Ishlatish
1. Datasetni yuklab oling Kaggle’dan va **UM_RACES.csv** nomi bilan saqlang.  
2. Skriptni ishga tushiring:

   Agar target ustuni `distance_km` bo‘lsa:
   ```bash
   python um_regression_pipeline.py --csv UM_RACES.csv --target distance_km
   ```

   Agar target boshqa nomda bo‘lsa, masalan `Distance`:
   ```bash
   python um_regression_pipeline.py --csv UM_RACES.csv --target Distance
   ```

3. Natijalar quyidagi fayllarda saqlanadi:
   - `um_best_model.joblib` → modelni qayta ishlatish uchun  
   - `um_metrics_report.json` → CV metrikalar (RMSE, MAE, R²)  
   - `um_feature_importance.png` → eng muhim featur’lar grafikasi  
   - `um_used_columns.json` → numeric va kategorik ustunlar ro‘yxati  

---

## 📊 Xususiyatlar (Features)
Model quyidagi ustunlardan foydalanadi (datasetga qarab):
- **Age** – Yosh  
- **Gender** – Jinsi  
- **Year** – Musobaqa yili  
- **Event / Race_type** – Musobaqa turi  
- **Country / Club** – Mamlakat yoki klub  

❌ Model `finish_time`, `speed` yoki **masofa bilan bevosita bog‘liq ustunlarni ishlatmaydi** (leakage oldini olish uchun).

---

## 🏆 Natijalar
Model bir nechta regressorlarda sinovdan o‘tkaziladi:
- Linear Regression (baseline)  
- Ridge Regression  
- RandomForest Regressor  
- HistGradientBoosting Regressor  

👉 Eng yaxshi model avtomatik tanlanadi va `.joblib` faylga saqlanadi.

---

## 📈 Keyingi Qadamlar
- Ko‘proq feature engineering (masalan, yosh guruhlari, mamlakat klasterlari).  
- Hiperparametrlarni yanada chuqurroq tuning qilish.  
- Modelni web-app yoki API ko‘rinishida joylash.  

---

✍️ **Muallif:** Rasulbek  
📅 **Loyiha sanasi:** 2025  
