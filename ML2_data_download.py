###############################################
#download data from yahoo! finance
###############################################

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 22:11:23 2017

@author: Jonas

data source: http://finance.yahoo.com/
"""

import pandas as pd
import yahoo_quote_download.yqd as yqd

from datetime import datetime

def get_stock(ticker, start, end):
    df = pd.DataFrame.from_csv(yqd.load_yahoo_quote(ticker, start, end))
    return df


#download data
#ibm = pdr.DataReader('IBM', 'yahoo', start=datetime(2014, 8, 1),
#                     end=datetime(2016, 11, 30))
#aapl = pdr.DataReader('AAPL', 'yahoo', start=datetime(2014, 8, 1),
#                      end=datetime(2016, 11, 30))
#fb = pdr.DataReader('FB', 'yahoo', start=datetime(2014, 8, 1),
#                    end=datetime(2016, 11, 30))
#googl = pdr.DataReader('GOOGL', 'yahoo', start=datetime(2014, 8, 1),
#                       end=datetime(2016, 11, 30))

ibm = get_stock('IBM', '20140801', '20161130')
aapl = get_stock('AAPL', '20140801', '20161130')
fb = get_stock('FB', '20140801', '20161130')
googl = get_stock('GOOGL', '20140801', '20161130')

#print first few lines of data
print(ibm.head())
print(aapl.head())
print(fb.head())
print(googl.head())

#export and save as csv files
ibm.to_csv('IBM_stock.csv', sep=',')
aapl.to_csv('Apple_stock.csv', sep=',')
fb.to_csv('Facebook_stock.csv', sep=',')
googl.to_csv('Google_stock.csv', sep=',')

