# ================================
# 2-DEADLINE: DATA CLEANING VA TAHLIL
# Dataset: wide_format_annual_surface_temp.csv
# ================================

# 1. Kutubxonalar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# ================================
# 2. DATASETNI YUKLASH
# ================================
df = pd.read_csv("C:\Users\ids\OneDrive\Documentos\GitHub\python-javoblari\Python\Python asoslari\python-#38\Amaliyot\wide_format_annual_surface_temp.csv")

print("Birinchi 5 qator:")
print(df.head())

print("\nMa'lumot haqida:")
print(df.info())

# ================================
# 3. DATA CLEANING
# ================================

# Bo‘sh qiymatlar
print("\nBo'sh qiymatlar:")
print(df.isnull().sum())

# To‘ldirish (sonli ustunlar uchun)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Qolgan bo‘shlarni o‘chirish
df.dropna(inplace=True)

# Dublikatlar
df.drop_duplicates(inplace=True)

print("\nTozalangandan keyin:")
print(df.info())

# ================================
# 4. NORMALIZATSIYA
# ================================
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

numeric_cols = df.select_dtypes(include=np.number).columns

df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

print("\nNormalizatsiyadan keyin:")
print(df.head())

# ================================
# 5. GRAFIK TAHLIL
# ================================

# 5.1 Histogram
df[numeric_cols].hist(figsize=(12, 8))
plt.suptitle("Histogramlar")
plt.show()

# 5.2 Boxplot
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[numeric_cols])
plt.title("Boxplot (Outlierlarni ko‘rish)")
plt.xticks(rotation=45)
plt.show()

# 5.3 Correlation Heatmap
corr = df[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# 5.4 Scatter Plot (birinchi 2 ustun)
if len(numeric_cols) >= 2:
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=df[numeric_cols[0]], y=df[numeric_cols[1]])
    plt.title(f"{numeric_cols[0]} vs {numeric_cols[1]}")
    plt.show()

# ================================
# 6. XULOSA
# ================================
print("\nXULOSA:")
print("✔ Bo‘sh qiymatlar tozalandi yoki to‘ldirildi")
print("✔ Dublikatlar olib tashlandi")
print("✔ Ma’lumotlar normalizatsiya qilindi (0-1 oralig‘ida)")
print("✔ Histogram, Boxplot, Heatmap va Scatter orqali tahlil qilindi")