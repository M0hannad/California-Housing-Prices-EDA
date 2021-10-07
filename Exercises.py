# Step: 0 -Importing all packages
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px


# Step: 1 -Importing the data

df = pd.read_csv('data/housing.csv')


# Step: 2 -Understanding the data

df.head()
df.info()
df.describe()


# Step: 3 -Fixing the missing values

df.isnull().sum()
df = df.fillna(method="ffill")

df.isnull().sum()


# Step: 4 -Statistical analysis

# Ocean proximity
sns.set_theme(style="dark")
sns.countplot(x="ocean_proximity", data=df, palette="prism")

# Median house value x ocean proximity
sns.barplot(x='ocean_proximity', y='median_house_value',
            data=df, palette="prism")

# Median Price of Houses in a block in $
plt.hist(df.median_house_value, bins=40, color='#E11439')
plt.xlabel('Median Price of Houses in a block in $')
plt.ylabel('Number of Houses')
plt.title('Average Distribution of Median Price of Housing')


# Step: 5 -Plotting the points on a map

# Sample of 300 Houses
df = df.sample(300)
r, c = df.shape
print("R:", r, "C:", c)

# Only Latitude and Longitude Features are required
df = df.iloc[:, 0:2]
print(*df.columns)

# Creating the map using plotly's express library

fig = px.scatter_mapbox(
    df, lat="latitude", lon="longitude", zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
