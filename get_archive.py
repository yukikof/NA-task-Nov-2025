# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
import requests 

def get_archive():
    url = "https://webarchive.nationalarchives.gov.uk/ukgwa/cdx?url=www.nhs.uk/conditions/coronavirus-covid-19&output=json"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}
    response = requests.get(url, headers = headers) #bypass 403 forbidden
    print(response.status_code)
    if response.status_code == 200:
        data = response.text       
        #last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        #price = data["Time Series (5min)"][last_refreshed]["1. open"]
        return data
    else:
        return "None"

i = get_archive()

print(i)
