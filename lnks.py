from supp_funcs import *

BBL12_17CSV = ['https://opendata.arcgis.com/datasets/82ab09c9541b4eb8ba4b537e131998ce_22.csv', 'https://opendata.arcgis.com/datasets/4c4d6b4defdf4561b737a594b6f2b0dd_23.csv',   'https://opendata.arcgis.com/datasets/d7aa6d3a3fdc42c4b354b9e90da443b7_1.csv',     'https://opendata.arcgis.com/datasets/a8434614d90e416b80fbdfe2cb2901d8_2.csv', 'https://opendata.arcgis.com/datasets/714d5f8b06914b8596b34b181439e702_36.csv',     'https://opendata.arcgis.com/datasets/c4368a66ce65455595a211d530facc54_3.csv',]
BBL12_17ZIP = ['https://opendata.arcgis.com/datasets/82ab09c9541b4eb8ba4b537e131998ce_22.zip', 'https://opendata.arcgis.com/datasets/4c4d6b4defdf4561b737a594b6f2b0dd_23.zip', 'https://opendata.arcgis.com/datasets/d7aa6d3a3fdc42c4b354b9e90da443b7_1.zip','https://opendata.arcgis.com/datasets/a8434614d90e416b80fbdfe2cb2901d8_2.zip', 'https://opendata.arcgis.com/datasets/714d5f8b06914b8596b34b181439e702_36.zip', 'https://opendata.arcgis.com/datasets/c4368a66ce65455595a211d530facc54_3.zip']

#Quarterly GDP
gdpDF = ['https://stats.oecd.org/sdmx-json/data/DP_LIVE/.QGDP.TOT.PC_CHGPP.Q/OECD?contentType=csv&amp;detail=code&amp;separator=comma&amp;csv-lang=en&amp;startPeriod=1980-Q1&amp;endPeriod=2017-Q3']

#Zones and Districts 
BIZ_Districts = ['https://opendata.arcgis.com/datasets/20ec5862d8f14bcbb9bf14f79c311406_15.csv','https://opendata.arcgis.com/datasets/20ec5862d8f14bcbb9bf14f79c311406_15.zip']
GS_GRANTS = ['https://opendata.arcgis.com/datasets/8f08535a1c144fdca6d8b8074cf92b35_34.csv',  'https://opendata.arcgis.com/datasets/8f08535a1c144fdca6d8b8074cf92b35_34.zip']
MS_CORRI = ['https://opendata.arcgis.com/datasets/8e602ef5080e4343913702452ddf71d4_16.csv',  'https://opendata.arcgis.com/datasets/8e602ef5080e4343913702452ddf71d4_16.zip', ]
GS_CORRI = ['https://opendata.arcgis.com/datasets/2ccac3f2585f487c9d14919d02d66740_13.csv', 'https://opendata.arcgis.com/datasets/2ccac3f2585f487c9d14919d02d66740_13.zip' ]
HIS_UND = [  'https://opendata.arcgis.com/datasets/3060b61b0f9c444dbbd873bfae5ffa16_21.csv','https://opendata.arcgis.com/datasets/3060b61b0f9c444dbbd873bfae5ffa16_21.zip',]
DDOT = ['https://opendata.arcgis.com/datasets/32143ca8983d4476b64f4202162bf61e_12.csv','https://opendata.arcgis.com/datasets/32143ca8983d4476b64f4202162bf61e_12.zip',]
NINV = ['https://opendata.arcgis.com/datasets/6da0781990494f678e9f5722e1c09a67_23.csv', 'https://opendata.arcgis.com/datasets/6da0781990494f678e9f5722e1c09a67_23.zip',]
IRB = ['https://opendata.arcgis.com/datasets/eac41c3a46274a6bbe6184c6bbf412e8_15.csv', 'https://opendata.arcgis.com/datasets/eac41c3a46274a6bbe6184c6bbf412e8_15.zip',]
DE = ['https://opendata.arcgis.com/datasets/27221bef23ed4f5aa6e8e51d51edede9_19.csv','https://opendata.arcgis.com/datasets/27221bef23ed4f5aa6e8e51d51edede9_19.zip',]
ED = ['https://opendata.arcgis.com/datasets/a3aefd57db394fd68d739556253dc44d_18.csv', 'https://opendata.arcgis.com/datasets/a3aefd57db394fd68d739556253dc44d_18.zip',]
SVZ = ['https://opendata.arcgis.com/datasets/67da6b571c5e41ec8c21b5ce54080434_1.csv','https://opendata.arcgis.com/datasets/67da6b571c5e41ec8c21b5ce54080434_1.zip', ]
DRZ = ['https://opendata.arcgis.com/datasets/900148002b174f13881ecd3961119d9c_17.csv', 'https://opendata.arcgis.com/datasets/900148002b174f13881ecd3961119d9c_17.zip',]
DTDEV = ['https://opendata.arcgis.com/datasets/ab5cc72b8eb3494abea8c848855e22c7_3.csv', 'https://opendata.arcgis.com/datasets/ab5cc72b8eb3494abea8c848855e22c7_3.zip',]

#Features 
LIQUOR = ['https://opendata.arcgis.com/datasets/cabe9dcef0b344518c7fae1a3def7de1_5.csv', 'https://opendata.arcgis.com/datasets/cabe9dcef0b344518c7fae1a3def7de1_5.zip',]
PHARM = ['https://opendata.arcgis.com/datasets/2335ba275c3f4320a3113f13181eab56_9.csv',     'https://opendata.arcgis.com/datasets/2335ba275c3f4320a3113f13181eab56_9.zip',]
GROC = ['https://opendata.arcgis.com/datasets/1d7c9d0e3aac49c1aa88d377a3bae430_4.csv','https://opendata.arcgis.com/datasets/1d7c9d0e3aac49c1aa88d377a3bae430_4.zip',]
AFH = ['https://opendata.arcgis.com/datasets/34ae3d3c9752434a8c03aca5deb550eb_62.csv','https://opendata.arcgis.com/datasets/34ae3d3c9752434a8c03aca5deb550eb_62.zip',]
SCF = ['https://opendata.arcgis.com/datasets/58562a06412e43b9acb2515010818b0a_28.csv', 'https://opendata.arcgis.com/datasets/58562a06412e43b9acb2515010818b0a_28.zip',]
FMKT = ['https://opendata.arcgis.com/datasets/f2e1c2ef9eb44f2899f4a310a80ecec9_2.csv',  'https://opendata.arcgis.com/datasets/f2e1c2ef9eb44f2899f4a310a80ecec9_2.zip',]
SVL = ['https://opendata.arcgis.com/datasets/67da6b571c5e41ec8c21b5ce54080434_0.csv','https://opendata.arcgis.com/datasets/67da6b571c5e41ec8c21b5ce54080434_0.zip',]
BANKS = ['https://opendata.arcgis.com/datasets/dfc51a5bd29347d0a2399743d3144d31_0.csv','https://opendata.arcgis.com/datasets/dfc51a5bd29347d0a2399743d3144d31_0.zip',]
CLUBS = ['https://opendata.arcgis.com/datasets/4589d3e500404dc5a648dcdf3bc2732e_29.csv', 'https://opendata.arcgis.com/datasets/4589d3e500404dc5a648dcdf3bc2732e_29.zip',]
HOTELS = ['https://opendata.arcgis.com/datasets/a3ed163dbf994792a010d742ef1f683d_6.csv', 'https://opendata.arcgis.com/datasets/a3ed163dbf994792a010d742ef1f683d_6.zip',]
SRV = ['https://opendata.arcgis.com/datasets/4a84fa926f234916b129cbc022ec4935_29.csv','https://opendata.arcgis.com/datasets/4a84fa926f234916b129cbc022ec4935_29.zip']
COFA = ['https://opendata.arcgis.com/datasets/ec634c5d3ce64a07bad5f74558acafcc_9.csv', 'https://opendata.arcgis.com/datasets/ec634c5d3ce64a07bad5f74558acafcc_9.zip',]
METRO = ['https://opendata.arcgis.com/datasets/54018b7f06b943f2af278bbe415df1de_52.zip'] 

ftrLst = [LIQUOR, PHARM, GROC, AFH, SCF, FMKT, SVL, BANKS, CLUBS, HOTELS, SRV, COFA, METRO]

#Construction and Financing
SUPR_TAX = ['https://opendata.arcgis.com/datasets/1c5d4b467eaa4301b976547c65cd7d06_24.csv', 'https://opendata.arcgis.com/datasets/1c5d4b467eaa4301b976547c65cd7d06_24.zip',]
TIF = ['https://opendata.arcgis.com/datasets/f60a6d54bf2e4e12a779fd0ba3a68e7e_26.csv', 'https://opendata.arcgis.com/datasets/f60a6d54bf2e4e12a779fd0ba3a68e7e_26.zip',]
BP12_17CSV = ['https://opendata.arcgis.com/datasets/d4891ca6951947538f6707a6b07ae225_5.csv','https://opendata.arcgis.com/datasets/81a359c031464c53af6230338dbc848e_37.csv', 'https://opendata.arcgis.com/datasets/5f4ea2f25c9a45b29e15e53072126739_7.csv', 'https://opendata.arcgis.com/datasets/4911fcf3527246ae9bf81b5553a48c4d_6.csv','https://opendata.arcgis.com/datasets/9ba1e2cc61144042bdde83b8c68f2580_34.csv','https://opendata.arcgis.com/datasets/981c105beef74af38cc4090992661264_25.csv', 'https://opendata.arcgis.com/datasets/5d14ae7dcd1544878c54e61edda489c3_24.csv',]
BP12_17ZIP = [ 'https://opendata.arcgis.com/datasets/4911fcf3527246ae9bf81b5553a48c4d_6.zip','https://opendata.arcgis.com/datasets/d4891ca6951947538f6707a6b07ae225_5.zip', 'https://opendata.arcgis.com/datasets/81a359c031464c53af6230338dbc848e_37.zip', 'https://opendata.arcgis.com/datasets/5f4ea2f25c9a45b29e15e53072126739_7.zip', 'https://opendata.arcgis.com/datasets/9ba1e2cc61144042bdde83b8c68f2580_34.zip', 'https://opendata.arcgis.com/datasets/981c105beef74af38cc4090992661264_25.zip', 'https://opendata.arcgis.com/datasets/5d14ae7dcd1544878c54e61edda489c3_24.zip',]
PUD = ['https://opendata.arcgis.com/datasets/bdfca0a8c4174bfab5fd1898c8860cc8_9.csv','https://opendata.arcgis.com/datasets/bdfca0a8c4174bfab5fd1898c8860cc8_9.zip',]

#Clim_data filepath
clim_flpath = ['./data/clim_data.csv']

#Extend this
supplm = [
    [zoneConcentration, [BIZ_Districts, 'BIZ_Dist_Concentr']],
    [zoneConcentration, [GS_GRANTS, 'GS_GRANTS_Concentr']],
    [zoneConcentration, [MS_CORRI, 'MS_CORRI_Concentr']],
    [zoneConcentration, [GS_CORRI, 'GS_CORRI_Concentr']],
    
    [pointInZone, [LIQUOR, 'LIQUOR_Concentr']],
    [pointInZone, [PHARM, 'PHARM_Concentr']],
    [pointInZone, [GROC, 'GROC_Concentr']],
    [pointInZone, [AFH, 'AFH_Concentr']],
    [oecdGdpQs,   gdpDF, 'i=i'],
    [metro_prox, None],
    [clim_ingest, clim_flpath[0], 'i=i'],
    
    
      ]



         
