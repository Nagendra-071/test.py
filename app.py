import streamlit as st
from datetime import date

import pandas as pd
import yfinance as yf
from  prophet  import Prophet
from prophet.plot import plot_plotly
import plotly.graph_objects as go


START="2015-01-01"
TODAY=date.today().strftime("%Y-%m-%d")

st.title("Stock visualizer App")

stocks=("AAPL","RELIANCE.NS","BANKNIFTY1.BO","HDB","IBN","SBIN.NS","HINDUNILVR.NS","INFY","BAJFINANCE.NS","LICI.NS","ITC.NS","LT.NS","MARUTI.NS","M&M.NS","HCLTECH.NS","KOTAKBANK.NS","SUNPHARMA.NS","ULTRACEMCO.NS","AXISBANK.BO","TITAN.NS","NTPC.NS","BAJAJFINSV.NS","DMART.NS","ONGC.NS","HAL.NS","ETERNAL.NS","ADANIPORTS.NS","BEL.NS","POWERGRID.NS","WIT","ADANIENT.NS","JSWSTEEL.NS","TATAMOTORS.NS","BAJAJ-AUTO.NS","ASIANPAINT.NS","COALINDIA.NS","ADANIPOWER.NS","NESTLEIND.NS","INDIGO.NS","TATASTEEL.NS","HYUNDAI.NS","JIOFIN.NS","IOC.NS","TRENT.NS","GRASIM.NS","DLF.NS","HINDZINC.NS","SBILIFE.NS","EICHERMOT.NS","VEDL.NS","VBL.NS","HDFCLIFE.NS","DIVISLAB.NS","HINDALCO.NS","TVSMOTOR.NS","IRFC.NS","PIDILITIND.NS","ADANIGREEN.NS","LTIM.NS","BAJAJHLDNG.NS","AMBUJACEM.NS","BRITANNIA.NS","BPCL.NS","TECHM.NS","GODREJCP.NS","PFC.NS","SOLARINDS.NS","CIPLA.NS","TATAPOWER.NS","BANKBARODA.NS","BOSCHLTD.NS","TORNTPHARM.NS","CHOLAFIN.NS","LODHA.NS","HDFCAMC.NS","PNB.NS","GAIL.NS","CGPOWER.NS","SIEMENS.NS","MAXHEALTH.NS","MUTHOOTFIN.NS","APOLLOHOSP.NS","INDHOTEL.NS","ABB.NS","MAZDOCK.NS","SHRIRAMFIN.NS","SHREECEM.NS","TATACONSUM.NS","POLYCAB.NS","DIXON.NS","HEROMOTOCO.NS","CUMMINSIND.NS","RDY","MANKIND.NS","JINDALSTEL.NS","ZYDUSLIFE.NS","MOTHERSON.NS","HAVELLS.NS","SWIGGY.NS","UNIONBANK.NS")
selected_stocks=st.selectbox("Seleect dataset fro prediction",stocks)


n_years=st.slider(" Period from 1 to 5 years:",1 , 5)
period=n_years * 365

@st.cache_data  #usign this we donot need to download data that has been previously seen
def load_data(ticker):
    data=yf.download(ticker,START,TODAY)
    data.reset_index(inplace=True)
    data['Date'] = pd.to_datetime(data['Date'])
    return data

data_load_state=st.text("Load data...")
data=load_data(selected_stocks)
data_load_state.text("LOading data...done!")


st.subheader('Raw data')
st.write(data.tail())


def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
    
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


plot_raw_data()

