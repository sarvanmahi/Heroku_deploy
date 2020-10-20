# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:12:04 2020

@author: ACAL
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())
