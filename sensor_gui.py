

import os
import pandas as pd
import streamlit as st
import time



if __name__ == '__main__':

  hist_file = './sensor_history.txt'

  title = st.title("Terrazita's temp humid")
  table = st.empty()
  chart = st.empty()

  while True:

    df_sensor_hist = pd.read_csv(hist_file, sep=' ')
    df_sensor_hist['timestamp'] = df_sensor_hist[['date', 'time']].apply(lambda x: ' '.join(x), axis=1)
    df_sensor_hist = df_sensor_hist.rename(columns={'timestamp':'index'}).set_index('index')
    df_sensor_hist = df_sensor_hist.drop(['date','time'], axis=1)

    print(df_sensor_hist)

    st.write(table.table(df_sensor_hist))
    st.write(chart.line_chart(df_sensor_hist))

    time.sleep(60*60)
  
  #st.table(df_sensor_hist)
  #st.line_chart(df_sensor_hist)


