import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.image as mpimg
import matplotlib.ticker as mtick

def load_housing_data():
    csv_path = os.path.join("11-November.csv")
    return pd.read_csv(csv_path)
housing = load_housing_data()
housing.head()

#To plot data on map image
california_img=mpimg.imread('map.png')
ax = housing.plot(kind="scatter", x="longitude", y="latitude", 
    s=70 , #This s is for marker size 
    #s=housing['PM-2.5 (ug/m3)'] (Use This when want to vary marker size with PM values)
    #label="PM-2.5 Data generated from Mobile Sensing by car (16/11/2020)",
    c="PM-2.5 (ug/m3)", cmap=plt.get_cmap("jet"), marker=".",
    colorbar=True, vmin=0, vmax=300, alpha=1, figsize=(13,8), legend=True)

#This contains both the figure and both the axis
fig = ax.figure
#Chossing the axis of colorbar with index position [1]
cb_ax = fig.axes[1] 
#Changing the font size of the colobar values
cb_ax.tick_params(labelsize=13)
#cb_ax.format(title='Axes legends')
# Changing the map axis font size
plt.tick_params(labelsize=12,width=1.5)

#To show data on Map
plt.imshow(california_img, extent=[75.73,75.805,26.9,26.96], alpha=1)

plt.xlabel("Longitude", fontsize=15)
plt.ylabel("Latitude", fontsize=15)

plt.show()

