import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV dosyasını oku
df = pd.read_csv("train.csv")

# Sayısal sütunları seç
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
x_column = numeric_cols[0]
y_column = numeric_cols[1]

# Çizgi Grafiği
plt.figure(figsize=(8, 5))
plt.plot(df[x_column], df[y_column], color='blue')
plt.title("Çizgi Grafiği")
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.show()

# Çubuk Grafiği
plt.figure(figsize=(8, 5))
plt.bar(df[x_column], df[y_column], color='red')
plt.title("Çubuk Grafiği")
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.show()

# Dağılım Grafiği
plt.figure(figsize=(8, 5))
plt.scatter(df[x_column], df[y_column], color='green')
plt.title("Dağılım Grafiği")
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.show()

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(df[y_column], bins=20, color='purple')
plt.title("Histogram")
plt.xlabel(y_column)
plt.ylabel("Frekans")
plt.show()
