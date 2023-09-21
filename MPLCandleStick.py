#%%
import pandas as pd
import mplfinance as mpf
#%%
df = 'NVDA.csv'
data = pd.read_csv(r"{area path for csv file}")
print(df)
# %%
data.Date = pd.to_datetime(data.Date)
data.info()
# %%
data = data.set_index('Date')

# %%
mpf.plot(data['2022-12': '2023-05'],type='candle',mav=(50) ,volume=True, figratio=(20,12), title='NVDA YTD', tight_layout=True)

# %%
