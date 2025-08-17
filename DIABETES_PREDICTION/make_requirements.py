import subprocess
import os

# 1. Faqat kerakli kutubxonalar ro'yxati
needed_libs = {
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "jupyter",
    "xgboost",
    "lightgbm",
    "catboost"
}

# 2. pip freeze natijasini olish
installed_packages = subprocess.check_output(["pip", "freeze"], text=True).split("\n")

# 3. Faqat keraklilarini filtr qilish
filtered_packages = [
    pkg for pkg in installed_packages
    if any(pkg.lower().startswith(lib.lower() + "==") for lib in needed_libs)
]

# 4. Hozirgi papkani olish (loyiha papkasi)
current_dir = os.getcwd()

# 5. Saqlash manzili
save_path = os.path.join(current_dir, "requirements.txt")

# 6. Faylni yozish
with open(save_path, "w") as f:
    f.write("\n".join(filtered_packages))

# 7. Yakuniy xabar
print("✅ requirements.txt yaratildi!")
print("📂 Saqlangan joy:", save_path)
