import pandas as pd
import numpy as np
import plotly.express as px

# CSV dosyasını oku
df = pd.read_csv("train.csv")

# Sayısal sütunları seç
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
x_column = numeric_cols[0]
y_column = numeric_cols[1]

# Çizgi Grafiği
fig1 = px.line(df, x=x_column, y=y_column, title="Çizgi Grafiği")
fig1.show()

# Çubuk Grafiği
fig2 = px.bar(df, x=x_column, y=y_column, title="Çubuk Grafiği")
fig2.show()

# Dağılım Grafiği
fig3 = px.scatter(df, x=x_column, y=y_column, title="Dağılım Grafiği")
fig3.show()

# Histogram
fig4 = px.histogram(df, x=y_column, nbins=20, title="Histogram")
fig4.show()
