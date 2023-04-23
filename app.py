import streamlit as sl
import pandas as pd
import plotly_express as px

df = pd.read_csv('./data/vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# Make Header above dataframe
sl.header('Data Viewer')
# display df with streamlit
sl.dataframe(df)

sl.header('Vehicle types by manufacturer')
# make a  plotly histogram
fig = px.histogram(df, x='manufacturer', color='type')
# display with sl
sl.write(fig)

sl.header('Histogram of `condition` vs `model_year')
fig = px.histogram(df, x='model_year', color='condition')
sl.write(fig)

sl.header('Compare price distribution between manufacturers')
manufac_list = sorted(df['manufacturer'].unique())
manufacturer_1 = sl.selectbox('Select manufacturer 1',
                              manufac_list, index=manufac_list.index('chevrolet'))

manufacturer_2 = sl.selectbox('Select manufacturer 2',
                              manufac_list, index=manufac_list.index('hyundai'))


mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]


normalize = sl.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None

fig = px.histogram(df_filtered,
                      x='price',
                      nbins=30,
                      color='manufacturer',
                      histnorm=histnorm,
                      barmode='overlay')

sl.write(fig)

