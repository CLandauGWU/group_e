def addr_shape(shapetype):
    #Process user-defined shapefile from DC OpenData
    
    import numpy as np
    import pandas as pd
    import geopandas as gpd
    
    assert shapetype == 'census' or 'ward' or 'anc' #Currently only supports these
    
    crs='EPSG:4326' #Convenience assignment of crs throughout
    
    if shapetype == 'census':
        shp_fl = down_extract_zip(
            'https://opendata.arcgis.com/datasets/6969dd63c5cb4d6aa32f15effb8311f3_8.zip'
        ) #Download the zip file and extract it, then assign the shapefile path
        shp_census = gpd.read_file(shp_fl, crs=crs)
        shp_df     = gpd.GeoDataFrame(shp_census,
                                  crs=crs,
                                  geometry=shp_census['geometry']
                                 )
        shp_df = shp_df.rename(columns={'TRACT': 'NAME'}) #Fix header

    
    if shapetype == 'ward':
        shp_fl = down_extract_zip(
            'https://opendata.arcgis.com/datasets/0ef47379cbae44e88267c01eaec2ff6e_31.zip'
        ) #Download the zip file and extract it, then assign the shapefile path
        shp_ward   = gpd.read_file(shp_fl, crs=crs)
        shp_df     = gpd.GeoDataFrame(shp_ward,
                                  crs=crs,
                                  geometry=shp_ward['geometry']
                                 )

    if shapetype == 'anc':
        shp_fl = down_extract_zip(
            'https://opendata.arcgis.com/datasets/fcfbf29074e549d8aff9b9c708179291_1.zip'
        ) #Download the zip file and extract it, then assign the shapefile path
        shp_anc    = gpd.read_file(shp_fl, crs=crs)
        shp_df     = gpd.GeoDataFrame(shp_anc,
                                  crs=crs,
                                  geometry=shp_anc['geometry']
                                 )
        
    
    adr_df  =pd.read_csv(
      './data/Address_Points.csv', encoding='utf-8', low_memory=False)

    return [adr_df, shp_df]

def down_extract_zip(url):
    #Downloads and unzips a DCopendata shape file
    #and returns the filepath of the shape file
    
    #Usage: must have file named 'data' in cwd.
    #Then: flname = down_extract_zip(url_of_zipfile)
    #flname is now the path of the shpfile.
    
    import os, zipfile, requests, time
    
    local_filename = str('./data/' + url.split('/')[-1])
        
    r = requests.get(url)
    
    while r.status_code != 200:
        print('Connection error: retrying...')
        time.sleep(10)
        r = requests.get(url)
    
    assert r.status_code == 200 #Check connection
    with open(local_filename, 'wb') as f:
        f.write(r.content)
    zip_fld = local_filename[:-4]
    if not os.path.exists(zip_fld):
        os.makedirs(zip_fld)
        with zipfile.ZipFile(local_filename, "r") as zip_pl:
            zip_pl.extractall(zip_fld)
    fld_arr = os.listdir(zip_fld) #get array of unzipped files
    for unzippedfile in fld_arr:  #find shapefile in unzipped files
        if str(unzippedfile[-3:]) == 'shp':
            flname = zip_fld + '/' + unzippedfile
    if not flname: 
        print('Shapefile not found!')
    return flname