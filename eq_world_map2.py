#building a world map

import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) #json.load returns a dict

all_eq_dicts =all_eq_data['features'] #put all data of earthquakes (located with key'features') in all_eq_dicts

#extracting magnitudes :
mags,lons,lats,hover_texts = [],[],[],[]
for eq_dict in all_eq_dicts: #eq_dict points to each dictionary about individual earthquake
    mag = eq_dict ['properties'] ['mag']
    mags.append(mag)

for eq_dict in all_eq_dicts:
    lon = eq_dict ['geometry'] ['coordinates'] [0]
    lons.append (lon)
    lat = eq_dict ['geometry'] ['coordinates'] [1]
    lats.append(lat)
    title = eq_dict ['properties'] ['title']
    hover_texts.append(title)

#map the earthquakes :
#data = [Scattergeo(lon=lons,lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker':{
        'size': [mag * 5 for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
        },
    }]

my_layout = Layout(title='Global Earthquakes')

fig = {'data':data, 'layout': my_layout}
offline.plot(fig,'global_earthquakes.html')