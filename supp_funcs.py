def zoneConcentration(shp_gdf, raw, pntLst, bufr=None):
    from downloading_funcs import addr_shape, down_extract_zip
    import pandas as pd
    import geopandas as gpd
    
    pnt          = pntLst[0]
    pnt_isCalled = pntLst[1]
    
    for url in pnt:
        if url[-3:] == 'zip':
            pnt = url
    assert isinstance(pnt, str) #Must extract a zipfile from pnt!
    
    #Convenience assignment of projection type
    crs='EPSG:4326'
    
    #Extract and read points into memory
    pnt = down_extract_zip(pnt)
    ftr = gpd.read_file(pnt, crs=crs)
    
    #Flag properties within distance "bufr" of featured locations 
    
    if not bufr:
        bufr = 1/250 #Hard to say what a good buffer is.
    
    assert isinstance(bufr, float) #buffer must be float!
    
    #Frame up the buffer shapes
    ftr.geometry = ftr.geometry.buffer(bufr)
    ftr['flag'] = 1
    if 'NAME' in ftr:
        ftr.drop(['NAME'], axis=1, inplace=True)
    
    #Frame up the raw address points data
    pointy         = raw[['NAME', 'Points', 'dummy_counter']]
    pointy         = gpd.GeoDataFrame(pointy, crs=ftr.crs, 
                                      geometry=pointy.Points)
    pointy         = gpd.sjoin(pointy, ftr, 
                               how='left', op='intersects')
    
    denom = pointy.groupby('NAME').sum()
    denom = denom.dummy_counter
    
    numer = pointy.groupby('NAME').sum()
    numer = numer.flag
    
    pct_ftr_coverage    = pd.DataFrame(numer/denom)
        
    pct_ftr_coverage.columns   = [
        pnt_isCalled
    ]
    
    pct_ftr_coverage.fillna(0, inplace=True)
    
    pct_ftr_coverage.crs = pointy.crs
    shp_gdf = shp_gdf.merge(pct_ftr_coverage,
                        how="left", left_on='NAME', right_index=True)
    del pct_ftr_coverage, raw, pointy, denom, numer
    return shp_gdf
    del shp_gdf

def pointInZone(shp_gdf, raw, zoneLst):
    from downloading_funcs import addr_shape, down_extract_zip
    import pandas as pd
    import geopandas as gpd
    
    
    zone          = zoneLst[0]
    zone_isCalled = zoneLst[1]
    
    for url in zone:
        if url[-3:] == 'zip':
            zone = url
    assert isinstance(zone, str) #Must extract a zipfile from pnt!
    
    #Convenience assignment of projection type
    crs='EPSG:4326'
    
    #Extract and read points into memory
    zone = down_extract_zip(zone)
    zone = gpd.read_file(zone, crs=crs)
    
    zone['flag'] = 1
    if 'NAME' in zone:
        zone.drop(['NAME'], axis=1, inplace=True)
        
    
    
    #Frame up the raw address points data
    pointy         = raw[['NAME', 'Points', 'dummy_counter']]
    pointy         = gpd.GeoDataFrame(pointy, crs=zone.crs, 
                                      geometry=pointy.Points)
    pointy         = gpd.sjoin(pointy, zone, 
                               how='left', op='intersects')
    
    
    numer = pointy.groupby('NAME').sum()
    numer = numer.flag
    
    inzone = pointy.groupby('NAME').sum()
    inzone = inzone.dummy_counter #This was calling denom.dummy_counter which is undeclared
    
    
    
    flaginzone   = pd.DataFrame(inzone)
        
    flaginzone.columns   = [
        zone_isCalled
    ]
    
    flaginzone.fillna(0, inplace=True)
    
    flaginzone.crs = pointy.crs
    shp_gdf = shp_gdf.merge(flaginzone,
                        how="left", left_on='NAME', right_index=True)
    del flaginzone, pointy, inzone, numer, raw
    return shp_gdf
    del shp_gdf

def oecdGdpQs(shp_gdf, raw, url, i=None):
    #This extracts U.S. GDP on a quarterly
    #basis to the correct time unit of analysis
    
    import numpy as np
    import pandas as pd
    import geopandas as gpd
    
    if not 'Q_GDP' in shp_gdf.columns:
        shp_gdf['Q_GDP'] = 0
        
    
    Qbins = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    
    yr    = round(i)
    q     = round((i-yr)*100)
    assert q < 14
    for ij in range(0, 4):
        if q in Qbins[ij]:
            q = 'Q'+ str(ij+1)
    
    
    df = pd.read_csv(url[0], encoding='utf-8')
    df = df[df.LOCATION == 'USA']

    
    df[['q', 'yr']]= df.Time.str.split('-', expand=True)
    
    df['q'] = df['q'].astype(str)
    df['yr'] = df['yr'].astype(int)
    
    df = df[(df.q == q)]
    df = df[(df.yr == yr)]
    i_gdp = list(df['Value'])
    
    i_gdp = i_gdp[0]
    
    shp_gdf['Q_GDP'][shp_gdf['month']==i] = i_gdp
    return shp_gdf
    del shp_gdf

def metro_prox(shp_gdf, raw, bufr=None):
    #Flag properties within distance "bufr" of metro stations
    
    from downloading_funcs import addr_shape, down_extract_zip
    import pandas as pd
    import geopandas as gpd
    
    if not bufr:
        bufr = 1/250 #Hard to say what a good buffer is.
    
    assert isinstance(bufr, float) #buffer must be float!
    
    #Frame up the metro buffer shapes
    metro = down_extract_zip(
    'https://opendata.arcgis.com/datasets/54018b7f06b943f2af278bbe415df1de_52.zip'
    )
    metro          = gpd.read_file(metro, crs=shp_gdf.crs)
    metro.geometry = metro.geometry.buffer(bufr)
    metro['bymet'] = 1
    metro.drop(['NAME'], axis=1, inplace=True)
    
    #Frame up the raw address points data
    pointy         = raw[['NAME', 'Points', 'dummy_counter']]
    pointy         = gpd.GeoDataFrame(pointy, crs=metro.crs, 
                                      geometry=pointy.Points)
    pointy         = gpd.sjoin(pointy, metro, 
                               how='left', op='intersects')
    
    denom = pointy.groupby('NAME').sum()
    denom = denom.dummy_counter
    
    numer = pointy.groupby('NAME').sum()
    numer = numer.bymet
    
    pct_metro_coverage    = pd.DataFrame(numer/denom)
        
    pct_metro_coverage.columns   = [
        'pct_metro_coverage'
    ]
    
    pct_metro_coverage.fillna(0, inplace=True)
    
    pct_metro_coverage.crs = pointy.crs
    shp_gdf = shp_gdf.merge(pct_metro_coverage,
                        how="left", left_on='NAME', right_index=True)
    return shp_gdf

def clim_ingest(shp_gdf, raw, filepath, i=None):
    #Adds monthly average, max and min temp, from National Airport
    
    import numpy as np
    import pandas as pd
    import geopandas as gpd
    
    #NOAA NCDC data mining is not worth implementing in this workflow
    #Pull the data from disk
    df = pd.read_csv(filepath)
    
    #Only want National Airport
    df = df[df.NAME == 'WASHINGTON REAGAN NATIONAL AIRPORT, VA US']
    
    #Express the dates as datetime objects
    df.DATE = pd.to_datetime(df.DATE)
    
    yr    = round(i)
    month = round((i-yr)*100)
    
    #Narrow it down to just the one row that matches "i"
    df = df[df.DATE.dt.year  == yr]
    df = df[df.DATE.dt.month == month]
    
    assert df.shape[0] == 1 #Only one row should match "i"
    
    for tag in ['TAVG', 'TMAX', 'TMIN']: #iterate thru values we want

        #Establishes the column if needed
        if not tag in shp_gdf.columns:   
            shp_gdf[tag] = 0
        #Extract the value of df[tag]
        val = list(df[tag])
        val = val[0]
        
        #Assign the extracted value to all shp_gdf[tag] rows where 'month' is t-i
        shp_gdf[tag][shp_gdf['month']==i] = val
        
    return shp_gdf
    del shp_gdf

def ITSPExtract(shp_gdf, raw, i=None):
    """Read in tax extract data, pare it down to month i,
    spatial join on the shape geodataframe shp_gdf. Return shp_gdf.
    """
    from downloading_funcs import addr_shape, down_extract_zip
    import pandas as pd
    from shapely.geometry import Point, Polygon
    import geopandas as gpd
    
    crs='EPSG:4326'
    
    df = pd.read_csv('./data/Integrated_Tax_System_Public_Extract.csv')
    
    df.SALEDATE = pd.to_datetime(df.SALEDATE)
    yr    = round(i)
    month = round((i-yr)*100)
    
    #Narrow it down to just the one row that matches "i"
    df = df[df.SALEDATE.dt.year  == yr]
    df = df[df.SALEDATE.dt.month == month]
    
    df = df.sort_values(['SALEDATE'])
    df = df.reset_index(drop=True)
    
    #ITSPE has no geospatial data, so we need to merge on addresspoints.
    adr_df = pd.read_csv('./data/Address_Points.csv')
    
    #Regex to clean off the regime codes and any other NaN.
    adr_df['SSL'] = adr_df['SSL'].str.replace(r'\D+', '')
    df['SSL'] = df['SSL'].str.replace(r'\D+', '')
    
    adr_df = pd.merge(adr_df, df, how='inner', on=['SSL', 'SSL'], suffixes=['', '_tax'])
    
    del df
    
    adr_df['geometry'] = [
        Point(xy) for xy in zip(
            adr_df.LONGITUDE.apply(float), adr_df.LATITUDE.apply(float)
        )
    ]
    
    adr_df = gpd.GeoDataFrame(adr_df, crs=shp_gdf.crs, geometry=adr_df.geometry)
    adr_df = adr_df.dropna(subset=['SALEPRICE'])
    
    pointy         = gpd.sjoin(shp_gdf, adr_df, 
                               how='left', op='intersects')
    
    pointy = pointy.dropna(subset=['SALEPRICE'])
    sales  = pointy.groupby('NAME').sum()
    sales  = sales.SALEPRICE
    
    sales.columns = ['realPropertySaleVolume'
        ]
    sales = pd.DataFrame(sales)
    
    shp_gdf = shp_gdf.merge(sales,
                        how="left", left_on='NAME', right_index=True)
    
    del sales, raw, pointy
    return shp_gdf
    del adr_df, shp_gdf