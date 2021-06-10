import streamlit as st
import yfinance as yf
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator
import datetime

st.title("Financial Dashboard")
st.write("""**Made by Aryan Tanwar - Using yfinance package**""")
st.write('Only 130 popular stocks ticker included')

option = st.sidebar.selectbox('Select one symbol', ( 'GOOG', 'AAPL', 'MSFT', 'GME', 'WISH', 'WISH', 'CLOV',
' WEN', 'BTC-USD', 'GOEV', 'GME', 'FSLY','AHT' , 'SENS', 'RIDE', 'KODK', 'ASTS', 'WKHS', 'MU', 'VLDR',
'APPN', 'AC.TO', 'LOTZ', 'AMZN', 'OPEN', 'NOKPF','SOFI', 'HYLN', 'RKT', 'SDC', 'SPWR', 'SIRI', 'ROOT', 'OTRK',
'WOOF', 'ABBV','ABT','ACN','ADBE','AIG','AMGN','AVGO','AXP','BA','BAC','BIIB','BK','BKNG','BLK','BMY','BRKB',
 'C','CAT','CHTR','CL','CMCSA','COF','COP','COST','CRM','CSCO','CVS','CVX','DD','DHR','DIS','DOW','DUK','EMR',
'EXC','F','FB','FDX','GD','GE','GILD','GM','GOOGL','GS','HD','HON','IBM','INTC','JNJ','JPM','KHC','KO','LIN',
'LLY','LMT','LOW','MA','MCD','MDLZ','MDT','MET','MMM','MO','MRK','MS','MSFT','NEE','NFLX','NKE','NVDA','ORCL',
'PEP','PFE','PG','PM','PYPL','QCOM','RTX','SBUX','SO','SPG','T','TGT','TMO','TMUS','TSLA','TXN','UNH','UNP',
'UPS','USB','V','VZ','WBA','WFC','WMT','XOM'))
today = datetime.date.today()
before = today - datetime.timedelta(days=700)
start_date = st.sidebar.date_input('Start date', before)
end_date = st.sidebar.date_input('End date', today)
if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')


df = yf.download(option,start= start_date,end= end_date, progress=False)

indicator_bb = BollingerBands(df['Close'])
bb = df
bb['bb_h'] = indicator_bb.bollinger_hband()
bb['bb_l'] = indicator_bb.bollinger_lband()
bb = bb[['Close','bb_h','bb_l']]

macd = MACD(df['Close']).macd()

rsi = RSIIndicator(df['Close']).rsi()

# Plot the prices and the bolinger bands
st.write('Stock Bollinger Bands')
st.line_chart(bb)
st.bar_chart(bb)
st.area_chart(bb)

progress_bar = st.progress(0)

# Plot MACD
st.write('Stock Moving Average Convergence Divergence (MACD)')
st.area_chart(macd)

# Plot RSI
st.write('Stock RSI ')
st.line_chart(rsi)

# Data of recent days
st.write('Recent data ')
st.dataframe(df.tail(10))