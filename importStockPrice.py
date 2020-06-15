from yahoo_fin import stock_info as si
import numpy as np

#import the list as string array
theList = np.genfromtxt("listStock_lq45.txt", dtype='str')

for ticker in theList:
        #at yahoo finance, the IDX stocks are marked with .jk at the end
        tickerjk = ticker+".jk"

        #get lowest 52 week
        stockPrice = si.get_stats("%s" % tickerjk)
        lowest = stockPrice.iloc[13,1]

        #get highest 52 week
        stockPrice = si.get_stats("%s" % tickerjk)
        highest = stockPrice.iloc[12,1
        
        #get current price
        livePrice = si.get_live_price(("%s" % tickerjk))
                
        #print altogether ticker, lowest, current and highest
        print(ticker, lowest, livePrice, highest)
