import pandas as pd
import numpy as np
from plotnine import ggplot, aes, geom_line, geom_bar, geom_point, geom_histogram
import matplotlib.pyplot as plt

# CSV dosyasını oku
df = pd.read_csv("train.csv")

# Sayısal sütunları seç
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
x_column = numeric_cols[0]
y_column = numeric_cols[1]

# Çizgi Grafiği
p1 = ggplot(df, aes(x=x_column, y=y_column)) + geom_line()
p1.draw()
plt.show()  # Matplotlib ile grafiği aç

# Çubuk Grafiği
p2 = ggplot(df, aes(x=x_column, y=y_column)) + geom_bar(stat="identity")
p2.draw()
plt.show()

# Dağılım Grafiği
p3 = ggplot(df, aes(x=x_column, y=y_column)) + geom_point()
p3.draw()
plt.show()

# Histogram
p4 = ggplot(df, aes(x=y_column)) + geom_histogram(bins=20)
p4.draw()
plt.show()
