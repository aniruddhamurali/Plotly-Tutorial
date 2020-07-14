import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
df.head()

# Select US only
df = df.loc[df['Country/Region'] == 'US']
# We only want the dates and case numbers
df = df.drop(['Province/State', 'Country/Region', 'Lat', 'Long'], axis=1)
# Transpose dataframe to put dates in one column and cases in another
df = df.transpose()
# Reset index so that dates column isn't used as the index
df.reset_index(level=0, inplace=True)
# Give names to the columns
df.columns = ['Date', 'Cases']

'''
fig = px.line(df, 
            x='Date', 
            y='Cases',
            title='COVID-19 Cases in the U.S. Over Time',
            hover_name='Date')
fig.show()
'''


import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(x=df['Date'], y=df['Cases'],
                                mode='markers'))

fig.update_layout(title='COVID-19 Cases in the U.S. Over Time',
                xaxis_title='Date',
                yaxis_title='Cases')

fig.show()
