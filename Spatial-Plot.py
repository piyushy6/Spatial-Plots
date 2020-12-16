import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import matplotlib.ticker as mtick
import numpy as np
      
#Image to be used as background      
california_img=mpimg.imread('Map.png')

#Reading CSV and its data
sensing = pd.read_csv('11-November.csv')

lat = sensing['latitude']
lon = sensing['longitude']
PM=sensing['PM-2.5 (ug/m3)']


sct=plt.scatter(x=lon, y=lat,c=PM, cmap='jet', 
                s=5,alpha=1,vmin=0, vmax=300)

plt.colorbar(fraction=0.01, pad=0.02).set_label(label='PM-2.5 (µg/m³)',size=13,weight='bold')
# fraction = Length of the colorbar
# pad = Distance of colorbar from the axis


fig = sct.figure
#Chossing the axis of colorbar with index [1]
cbar = fig.axes[1] 
#Changing the font size of the colobar values
cbar.tick_params(labelsize=13)

# Changing the map axis font size
plt.tick_params(labelsize=13,width=1.5)

# yticks for y axis coordinates frequency
#plt.yticks(np.arange(min(lat)-1, max(lat)+1, difference = 0.001))
plt.yticks(np.arange(26.935, 26.955+1, 0.01))

plt.imshow(california_img,extent=[75.71,75.805,26.935,26.955], interpolation='sinc',aspect=1)


#plt.axis(aspect='equal')
plt.xlabel('Longitude',fontsize=15)
plt.ylabel('Latitude',fontsize=15)

plt.show()
