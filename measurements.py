%matplotlib inline
import geopandas as gpd

buowl = gpd.read_file("data/BUOWL_Habitat.shp")
raptors = gpd.read_file("data/Raptor_Nests.shp")
linears = gpd.read_file("data/Linear_Projects.shp")

buowl['area_2163']=buowl['geometry'].area/10000
buowl.head(10)

buowl = buowl.to_crs(epsg=26913)

buowl['area_26913']=buowl['geometry'].area/10000
buowl.head()

buowl['area_diff']=(buowl['area_26913']-buowl['area_2163'])/buowl['area_2163']*100
buowl.describe()

buowl['perimeter'] = buowl['geometry'].length
buowl.head()

buowl['min_perimeter'] = (buowl['geometry'].area/3.14159)**0.5*3.14159*2
buowl.head()

buowl["perimeter_ratio"] = buowl['perimeter']/buowl['min_perimeter']
buowl.head()

buowl.sort_values('perimeter_ratio', ascending=False)

buowl[buowl['habitat_id']==378].plot()

linears.crs

linears['length']=linears['geometry'].to_crs(epsg=26913).length
linears

raptors['area']=raptors['geometry'].area
raptors['length']=raptors['geometry'].length
raptors
