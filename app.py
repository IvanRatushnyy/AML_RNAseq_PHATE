#Import plotly and dash for graphing and layout. Pandas/numpy to work with data. PHATE for calculating coordinates
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
import pandas as pd
#import numpy as np
#import phate


#Dataframe of annotations
annotations = pd.read_csv("data/TARGET_AML_annotations.csv")

#Use first column as row names
annotations = annotations.set_index("donorID")
annotations.index.names = [None]
annotations = annotations.sort_index()

#Initialize arrays which will store the x, y and z coordinates for the graph
x = []
y = []
z = []

#Loop through lines and add coordinates to arrays
i = 1
with open("data/coordinates.csv", "r") as f:
    for line in f:
        if i == 1:
            x.append(float(line.strip()))
            i += 1
        elif i == 2:
            y.append(float(line.strip()))
            i +=1
        else:
            z.append(float(line.strip()))
            i = 1


#Intersections between data and annotations
intersection = []
with open("data/intersection.csv", "r") as f:
  for line in f:
    intersection.append(line.strip())


#Reusing px.colors.qualitative, so define as a variable.
qualitative = px.colors.qualitative

#Name and values of all discrete colors built into Plotly. 
#Predefined arrays needed because of the limited methods that px.colors.discrete has. First array contains names for the dropdown (color values would not show up), second contains values of the colors (cannot reference a value given a string).
discrete_color_names = ["Plotly", "D3", "G10", "T10", "Alphabet", "Dark24", "Light24", "Set1", "Pastel1", "Dark2", "Set2", "Pastel2", "Set3", "Antique", "Bold", "Pastel", "Prism", "Safe", "Vivid"]
discrete_colors = [qualitative.Plotly, qualitative.D3, qualitative.G10, qualitative.T10, qualitative.Alphabet, qualitative.Dark24, qualitative.Light24, qualitative.Set1, qualitative.Pastel1, qualitative.Dark2, qualitative.Set2, qualitative.Pastel2, qualitative.Set3, qualitative.Antique, qualitative.Bold, qualitative.Pastel, qualitative.Prism, qualitative.Safe, qualitative.Vivid]

#Our dash application
app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1(children='PHATE'),

        html.H2(children='Dimensions'),
        dcc.RadioItems(id='dimensions', options=['2D', '3D'], value='2D'),

        html.H2(children='Selected annotation'),
        dcc.Dropdown(id='annotation', options=annotations.transpose()[intersection].index, value='Age.in.years', clearable=False),

        html.H2(children='Discrete color'),
        dcc.Dropdown(id='discrete', options=discrete_color_names, value='Plotly', clearable=False),

        html.H2(children='Continuous color'),
        dcc.Dropdown(id='continuous', options=px.colors.named_colorscales(), value='aggrnyl', clearable=False),

        html.H2(children='Dot opacity'),
        dcc.Slider(id='opacity', min=0.1, max=1.0, value=0.8, marks={0.1: {'label': '0.1'}, 1: {'label': '1'}}),

        html.H2(children='Dot size'),
        dcc.Slider(id='dot_size', min=2, max=15, value=8, marks={2: {'label': '2'}, 15: {'label': '15'}})
    ], className='sidebar'),

    html.Div([
        dcc.Graph(id='graph')
    ], className='main')
])

@app.callback (
    Output('graph', 'figure'),

    Input('dimensions', 'value'),

    Input('annotation', 'value'),

    Input('discrete', 'value'),
    Input('continuous', 'value'),

    Input('opacity', 'value'),
    Input('dot_size', 'value')
)

def update_figure(dimensions, annotation, discrete, continuous, opacity, dot_size):

    current_annotation = annotations.transpose()[intersection].loc[annotation]

    if isint(current_annotation[0]) or isfloat(current_annotation[0]):
        current_annotation = current_annotation.astype(float)
    else:
        current_annotation = current_annotation.astype(str)

    discrete

    if dimensions == '3D':
        fig = px.scatter_3d(x=x, y=y, z=z, color=current_annotation, color_continuous_scale=continuous, color_discrete_sequence=discrete_colors[discrete_color_names.index(discrete)], opacity=opacity)
    else:
        fig = px.scatter(x=x, y=y, color=current_annotation, color_continuous_scale=continuous, color_discrete_sequence=discrete_colors[discrete_color_names.index(discrete)], opacity=opacity)

    return fig.update_traces(marker={'size': dot_size})

def isint(string):
    try:
        int(string)
        return True
    except:
        return False

def isfloat(string):
    try:
        float(string)
        return True
    except:
        return False

if __name__ == '__main__':
    app.run_server(debug=True)
