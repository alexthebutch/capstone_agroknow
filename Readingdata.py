#!/usr/bin/env python
# coding: utf-8

# In[127]:


import pandas as pd
import requests
import json
from keys import config


url = config['url']

headers = {
  'Content-Type': 'application/json',
  'Cookie': '__cfduid=d368dcf09d47170e4963d103f7fdaf48b1595250587'}


my_data = pd.DataFrame([])

for i in range(99):
    
    payload = {"apikey": config["apikey"],
           "entityType": "incident",
           "published": True, "detail": True,
            "pageSize":1000, "page":i}
        
        
    response = requests.request("POST", url, headers=headers, data = json.dumps(payload)).json()
    
    first_data = [(x['_source']['description'],x['_source']['remoteTitle'],x['_source']['hazardCategories'][0]['value'],) for x in response['hits']['hits']]
    first_df = pd.DataFrame(first_data, columns=['Description','Remote Title', 'Hazard Type'])
    
    my_data= my_data.append(first_df,ignore_index=True)
        
    


# In[133]:


my_data.to_csv('cp_data.csv', encoding='utf-8')

