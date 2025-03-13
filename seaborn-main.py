import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# CSV dosyasını oku
df = pd.read_csv("train.csv")

# Sayısal sütunları seç
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
x_column = numeric_cols[0]
y_column = numeric_cols[1]

# Çizgi Grafiği
plt.figure(figsize=(8, 5))
sns.lineplot(x=df[x_column], y=df[y_column])
plt.title("Çizgi Grafiği")
plt.show()

# Çubuk Grafiği
plt.figure(figsize=(8, 5))
sns.barplot(x=df[x_column], y=df[y_column])
plt.title("Çubuk Grafiği")
plt.show()

# Dağılım Grafiği
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df[x_column], y=df[y_column])
plt.title("Dağılım Grafiği")
plt.show()

# Histogram
plt.figure(figsize=(8, 5))
sns.histplot(df[y_column], bins=20, kde=True)
plt.title("Histogram")
plt.show()
