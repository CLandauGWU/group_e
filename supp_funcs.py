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
    return shp_gdf

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
    
    #Convenience assignment of projection type
    crs='EPSG:4326'
    
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
    return shp_gdf

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

