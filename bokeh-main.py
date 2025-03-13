import pandas as pd
import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.layouts import column
from bokeh.models import ColumnDataSource

# CSV dosyasını oku
df = pd.read_csv("train.csv")

# Sayısal sütunları seç
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

if len(numeric_cols) < 2:
    raise ValueError("En az iki sayısal sütun gerekli!")

x_column = numeric_cols[0]  # İlk sayısal sütun (X ekseni)
y_column = numeric_cols[1]  # İkinci sayısal sütun (Y ekseni)

# HTML dosyası olarak kaydetme
output_file("bokeh_visualizations.html")

# Veriyi Bokeh için uygun hale getir
source = ColumnDataSource(df)

### 1️⃣ Çizgi Grafiği (Line Plot)
line_plot = figure(title="Çizgi Grafiği", x_axis_label=x_column, y_axis_label=y_column, width=600, height=400)
line_plot.line(df[x_column], df[y_column], line_width=2, color="blue", legend_label="Çizgi")

### 2️⃣ Çubuk Grafiği (Bar Chart)
bar_plot = figure(title="Çubuk Grafiği", x_axis_label=x_column, y_axis_label=y_column, width=600, height=400)
bar_plot.vbar(x=df[x_column], top=df[y_column], width=0.5, color="red", legend_label="Çubuklar")

### 3️⃣ Dağılım Grafiği (Scatter Plot)
scatter_plot = figure(title="Dağılım Grafiği", x_axis_label=x_column, y_axis_label=y_column, width=600, height=400)
scatter_plot.circle(df[x_column], df[y_column], size=7, color="green", alpha=0.6, legend_label="Dağılım")

### 4️⃣ Histogram (Histogram)
hist, edges = np.histogram(df[y_column], bins=20)
hist_plot = figure(title="Histogram", x_axis_label=y_column, y_axis_label="Frekans", width=600, height=400)
hist_plot.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="purple", line_color="black", legend_label="Histogram")

### 5️⃣ Alan Grafiği (Area Plot)
area_plot = figure(title="Alan Grafiği", x_axis_label=x_column, y_axis_label=y_column, width=600, height=400)
area_plot.varea(x=df[x_column], y1=df[y_column] * 0.8, y2=df[y_column] * 1.2, fill_color="orange", alpha=0.4, legend_label="Alan")

### 6️⃣ Kutu Grafiği (Box Plot)
q1 = df[y_column].quantile(0.25)
q2 = df[y_column].quantile(0.50)
q3 = df[y_column].quantile(0.75)
iqr = q3 - q1
upper_whisker = q3 + 1.5 * iqr
lower_whisker = q1 - 1.5 * iqr
box_plot = figure(title="Kutu Grafiği (Box Plot)", width=600, height=400)
box_plot.segment(x0=[1], y0=[lower_whisker], x1=[1], y1=[upper_whisker], line_width=2, color="black")
box_plot.vbar(x=[1], width=0.4, top=q3, bottom=q1, fill_color="cyan", alpha=0.7)
box_plot.circle([1], [q2], size=10, color="red")

# Tüm grafikleri tek sayfada göster
show(column(line_plot, bar_plot, scatter_plot, hist_plot, area_plot, box_plot))
