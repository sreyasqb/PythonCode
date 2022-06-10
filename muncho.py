import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="MyApp")
# location = geolocator.geocode("273, Monalisa, 6th Main, 100 Feet Road, Indiranagar, Defence Colony, Indiranagar, Bangalore")
# print(location.latitude,location.longitude)
data=pd.read_csv('D:\RandomData\zomatoData.csv')
data=pd.DataFrame(data)
data=data.replace('-','0')
# print(data.iloc[[5]]['Dinner Ratings'])
filtered_data=data[['Name','Area','Dinner Ratings','Dinner Reviews','AverageCost']]
filtered_data=filtered_data.sort_values(by=['Area'])
# print(filtered_data.head())


areaGroup=filtered_data.groupby('Area').agg({'Dinner Reviews':'mean','AverageCost':'mean','Area':'count'})
# areaGroup=filtered_data.value_counts(subset=['Area'])
areaGroup.index.name=None
areaGroup=areaGroup.sort_values(by=['Area'],ascending=False)

# print(areaGroup['Area'])
# print(areaGroup.head(50))

pkf=data['PeopleKnownFor']
words=[]
for i in pkf:
    # print(i)
    if i==i:
        # print(i.split(','))
        for j in i.split(','):
            if j.strip() not in words:
                words.append(j.strip())
# print(pkf)
print(words)
# areaGroup.head(50).to_csv("regions.csv")
# print(areaGroup['Area'])
# print(areaGroup.head(n=10).to_string(index=False))
