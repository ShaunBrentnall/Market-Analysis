import pandas as pd
import numpy as np
import requests

def getdata(url):
  r = requests.get(url,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}, verify=False)
  data = pd.read_html(r.text)
  return data

ticker = "AAPL"

summary_url = f'https://finance.yahoo.com/quote/{ticker}.AX?p={ticker}.AX&.tsrc=fin-srch'
summary_data = getdata(summary_url)

print(summary_data)