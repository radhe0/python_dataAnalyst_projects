# 🏠 Airbnb Listings EDA & Data Visualization - New York 2024

## 📌 Project Overview

This project performs an exploratory data analysis (EDA) on Airbnb listings in New York City. The aim is to uncover pricing trends, host behavior, and property insights using data visualization techniques.

## 🔍 Key Objectives:

- Analyze pricing distribution across different boroughs.

- Identify factors influencing Airbnb pricing.

- Explore host activity and property availability trends.

- Communicate findings effectively through data visualizations.

## 📊 Dataset Information:

- Source: Airbnb Open Data 2024

- Features Include:

- Property details (price, room type, availability, etc.)

- Host information (host ID, number of listings, etc.)

- Location details (neighborhood, latitude, longitude, etc.)

- Guest feedback (number of reviews, review scores, etc.)

## 📜 Project Workflow

### 1️⃣ Importing Dependencies

To ensure all necessary libraries are installed, use the following:
```python
pip install pandas numpy matplotlib seaborn folium
```

Then, import them into your Python script:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
%matplotlib inline
```
### 2️⃣ Loading the Dataset
```python
data = pd.read_csv('datasets.csv', encoding_errors='ignore')
```
### 3️⃣ Initial Data Exploration
```python
data.head()
data.sample()
data.shape
data.info()
```
### 4️⃣ Data Cleaning & Preprocessing

Check for missing values and duplicates:
```python
missing_values = data.isnull().sum()
missing_values[missing_values > 0]
```
Remove duplicate rows:
```python
data.drop_duplicates(inplace=True)
```
Handle missing values:
```python
data.dropna(inplace=True)  # Removing rows with missing values
```
Check and adjust data types:
```python
data.dtypes
```
## 📈 Exploratory Data Analysis (EDA)

### ✅ Summary Statistics
```python
data.describe()
```
### ✅ Correlation Heatmap
```python
corr = data.corr()
plt.figure(figsize=(8,6))
sns.heatmap(data=corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()
```


### ✅ Price Distribution Analysis
```python
sns.boxplot(data=data, x='price')
```
Observation: Some listings have extremely high prices, which need to be handled as outliers.

To remove outliers:
```python
data = data[data['price'] < 1500]
```
After outlier removal:
```python
plt.figure(figsize=(8,5))
sns.histplot(data=data, x='price', bins=100)
plt.title("Price Distribution")
plt.ylabel("Frequency")
plt.show()
```


### ✅ Availability Distribution
```python
plt.figure(figsize=(8,5))
sns.histplot(data=data, x='availability_365')
plt.title("Availability 365 Distribution")
plt.ylabel("Frequency")
plt.show()
```
### ✅ Neighborhood-Wise Pricing Analysis
```python
data.groupby(by='neighbourhood_group')['price'].mean()
```
### ✅ Feature Engineering: Price Per Bed
```python
data['price_per_bed'] = data['price'] / data['beds']
data.groupby(by='neighbourhood_group')['price_per_bed'].mean()
```
### ✅ Bi-Variable Analysis

Room Type & Price
```python
sns.barplot(data=data, x='neighbourhood_group', y='price', hue='room_type')
```
Number of Reviews & Price
```python
plt.figure(figsize=(8,5))
plt.title("Locality and Review Dependencies")
sns.scatterplot(data=data, x='number_of_reviews', y='price', hue='neighbourhood_group')
```
### ✅ Geospatial Analysis
```python
plt.figure(figsize=(10,7))
sns.scatterplot(data=data, x='longitude', y='latitude', hue='room_type')
plt.title("Geographical Distribution of Airbnb Listings")
plt.show()
```
### ✅ Top 10 Hosts by Number of Listings
```python
top_hosts = data['host_id'].value_counts().head(10)
plt.figure(figsize=(13,6))
sns.barplot(x=top_hosts.index, y=top_hosts.values, palette="magma")
plt.title("Top 10 Hosts with Most Listings")
plt.xlabel("Host ID")
plt.ylabel("Number of Listings")
plt.show()
```


### ✅ Airbnb Listings on a Map (Using Folium)
```python
map_nyc = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
for _, row in data.sample(500).iterrows():  # Sample 500 listings to avoid clutter
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=3,
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(map_nyc)
map_nyc
```
## 📌 Key Insights

**1.Pricing Trends:**

 - Prices vary significantly by borough, with Manhattan being the most expensive.

 - There are extreme price outliers that require filtering for accurate analysis.

**2.Host Behavior:**

 - Certain hosts have significantly higher numbers of listings.

 - Most listings are from individual hosts rather than corporate ones.

**3.Room Type Preferences:**

 - Entire home/apartments tend to have higher prices.

 - Private and shared rooms are more affordable but less available in certain boroughs.

**4.Geospatial Insights:**

 - Listings are densely populated around Manhattan and Brooklyn.

 - High review counts correlate with lower-priced properties.

## 📌 Conclusion

This project provided key insights into Airbnb listings in New York City. It highlights pricing patterns, host activity, and geographic trends. The use of data visualization was crucial in drawing meaningful conclusions.

## 📌 Future Enhancements

Machine Learning: Predicting prices based on various features.

Time Series Analysis: Studying seasonal trends in Airbnb pricing.

More Advanced Mapping: Using interactive maps to visualize data dynamically.

## 📌 Author

**Ravi Yadav** 
 Data Analyst | Data Engineer | Airbnb Data Enthusiast
 📧 yravi8804@gmail.com

## 📌 Acknowledgments

This analysis is based on publicly available Airbnb data. Special thanks to the contributors of open-source data science libraries.

🚀 Feel free to explore and enhance this project!

