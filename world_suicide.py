import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

suicide_data = pd.read_csv('suicide1.csv')

# checking head of the suicide_data
print(suicide_data.head())

# creating data object of type choropleth
data = dict(
						type = 'choropleth',
						locations = suicide_data['country'],
						locationmode = 'country names',
						colorscale = 'Portland',
						colorbar = { 'title':'Suicide Number' },
						z = suicide_data['suicides_no'],
						text = suicide_data['country']
					)


layout = dict(
							title = 'Human Suicide Rate',
							geo = dict(
													showlakes = True,
													lakecolor = 'rgb(25,25,25)'
												)
						)


world_map = go.Figure(data=[data], layout=layout)

iplot(world_map)
