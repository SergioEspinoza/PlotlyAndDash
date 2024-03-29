#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:

import pandas as pd

import plotly.graph_objs as go
import plotly.offline as pyo

# Create a pandas DataFrame from 2010YumaAZ.csv
raw_df = pd.read_csv('../Data/2010YumaAZ.csv')
print( raw_df.head() )

days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']

# Use a for loop (or list comprehension to create traces for the data list)
dfs = [  raw_df.loc[ raw_df ['DAY'] == day, ['DAY', 'LST_TIME', 'T_HR_AVG' ] ]  for day in days  ]

data = []

for df in dfs:
    day = df['DAY'].values[0]
    print( ' **** {} **** '.format(day) )
    data.append( go.Scatter( x = df['LST_TIME'],
                             y = df[ 'T_HR_AVG' ],
                             mode='lines',
                             name=day ) )



#for day in days:
    # What should go inside this Scatter call?
#    trace = go.Scatter()
#    data.append(trace)

# Define the layout

layout = go.Layout( title='week temp' )

# Create a fig from data and layout, and plot the fig

figure = go.Figure( data = data, layout = layout )


pyo.plot(  figure )
