# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import json
import requests 
import pandas as pd
# %%

def get_archive(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}
    response = requests.get(url, headers = headers) #bypass 403 forbidden
    #print(response.status_code)
    if response.status_code == 200:
        data = response.text       
        return data
    else:
        return "None"
# %%
url1 = "https://webarchive.nationalarchives.gov.uk/ukgwa/cdx?url=www.nhs.uk/conditions/coronavirus-covid-19&output=json"
url2 = "https://webarchive.nationalarchives.gov.uk/ukgwa/cdx?url=www.nhs.uk/conditions/covid-19&output=json"
url3 = "https://webarchive.nationalarchives.gov.uk/ukgwa/cdx?url=www.nhs.uk/conditions/wuhan-novel-coronavirus/&output=json"

i = get_archive(url1)
j = get_archive(url2)
k = get_archive(url3)

# %%
def create_df(r):
    resp_json = []
    ndjson = r.split('\n')
    
    for json_obj in ndjson:
        if json_obj:
            resp_json.append(json.loads(json_obj))
    
    df = pd.DataFrame(resp_json)
    
    return(df)

# %%
#data cleaning

df_cvs = create_df(i)
df_c19 = create_df(j)
df_ncv = create_df(k)

df_cvs['urltail'] = "coronavirus-covid-19"
df_c19['urltail'] = "covid-19"
df_ncv['urltail'] = "wuhan-novel-coronavirus" 
#I could've used the url field but I figured this might be cleaner

df_all = pd.concat([df_cvs,df_c19,df_ncv])
#print(df_all)

df_all.timestamp = pd.to_datetime(df_all.timestamp)
#df_all['year'] = df_all['timestamp'].dt.year
#df_all['month'] = df_all['timestamp'].dt.month
#df_all['ym'] = df_all['year'].astype(str)+df_all['month'].astype(str)

df_all.to_csv("df_all.csv",index=False,header=True)

#%%

