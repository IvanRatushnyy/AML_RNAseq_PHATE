#Import plotly and dash for graphing and layout. Pandas/numpy to work with data. PHATE for calculating coordinates
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Dash, html, dcc, Input, Output
import pandas as pd
#import numpy as np
#import phate

#Initialize arrays which will store the x, y and z coordinates for each visualization type
#PHATE
x_phate = []
y_phate = []
z_phate = []

#PCA
x_pca = []
y_pca = []
z_pca = []

#tSNE
x_tsne = []
y_tsne = []
z_tsne = []

#UMAP
x_umap = []
y_umap = []
z_umap = []

#Lists of names
file_names = ['phate_coordinates.csv', 'pca_coordinates.csv', 'tsne_coordinates.csv', 'umap_coordinates.csv']
visualization_names = ['PHATE', 'PCA', 'tSNE', 'UMAP']
discrete_color_names = ['Plotly', 'D3', 'G10', 'T10', 'Alphabet', 'Dark24', 'Light24', 'Set1', 'Pastel1', 'Dark2', 'Set2', 'Pastel2', 'Set3', 'Antique', 'Bold', 'Pastel', 'Prism', 'Safe', 'Vivid']

#Lists of variables
coordinates = [[x_phate, y_phate, z_phate], [x_pca, y_pca, z_pca], [x_tsne, y_tsne, z_tsne], [x_umap, y_umap, z_umap]]

qualitative = px.colors.qualitative
discrete_colors = [qualitative.Plotly, qualitative.D3, qualitative.G10, qualitative.T10, qualitative.Alphabet, qualitative.Dark24, qualitative.Light24, qualitative.Set1, qualitative.Pastel1, qualitative.Dark2, qualitative.Set2, qualitative.Pastel2, qualitative.Set3, qualitative.Antique, qualitative.Bold, qualitative.Pastel, qualitative.Prism, qualitative.Safe, qualitative.Vivid]


#Dataframe of annotations
annotations = pd.read_csv('dash/data/TARGET_AML_annotations.csv')

#Use first column as row names
annotations = annotations.set_index('donorID')
annotations.index.names = [None]
annotations = annotations.sort_index()

#Remove unnecessary annotations
annotations.drop('Comment', 1)


#Loop through lines and add coordinates to arrays
for name in file_names:
    with open('dash/data/coordinates/'+name, 'r') as file:
        index = 0

        for line in file:
            coordinates[file_names.index(name)][index].append(float(line.strip()))

            index += 1
            if index > 2: index = 0

#Intersections between data and annotations
intersection = []
with open('dash/data/intersection.csv', 'r') as f:
  for line in f:
    intersection.append(line.strip())

#Sort intersection in order for annotations to line up with coordinate data
intersection.sort()


#Reusing px.colors.qualitative, so define as a variable.
qualitative = px.colors.qualitative

#Name and values of all discrete colors built into Plotly. 
#Predefined arrays needed because of the limited methods that px.colors.discrete has. First array contains names for the dropdown (color values would not show up), second contains values of the colors (cannot reference a value given a string).



#Our dash application
app = Dash(__name__)

#The layout of our app, or how it looks
app.layout = html.Div([
    html.Div([
        html.H1(children='AML RNA Seq'),

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

#All input and output callbacks, in our case we update the graph based on values such as opacity
@app.callback (
    Output('graph', 'figure'),

    Input('dimensions', 'value'),

    Input('annotation', 'value'),

    Input('discrete', 'value'),
    Input('continuous', 'value'),

    Input('opacity', 'value'),
    Input('dot_size', 'value')
)

#Function which will update our figure based on the inputs that are passed in
def update_figure(dimensions, annotation, discrete, continuous, opacity, dot_size):

    current_annotation = annotations.transpose()[intersection].loc[annotation]

    if isfloat(current_annotation[0]):
        current_annotation = current_annotation.astype(float)
    else:
        current_annotation = current_annotation.astype(str)

    fig = make_subplots(rows=2, cols=2)
    if dimensions == '3D': fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'scatter3d'}, {'type': 'scatter3d'}], [{'type': 'scatter3d'}, {'type': 'scatter3d'}]])

    for index in range(4):
        x = coordinates[index][0]
        y = coordinates[index][1]
        z = coordinates[index][2]

        row = (index+1 - 1) // 2 + 1
        col = (index+1 - 1) % 2 + 1

        current_name = visualization_names[index]

        if dimensions == '3D':
            pxgraph = px.scatter_3d(x=x, y=y, z=z, color=current_annotation, color_discrete_sequence=discrete_colors[discrete_color_names.index(discrete)], opacity=opacity)
            graph = go.Figure(pxgraph.to_dict())

            graph.update_traces(marker={'size': dot_size})
            fig.add_traces(graph.data, rows=row, cols=col)
        else:
            pxgraph = px.scatter(x=x, y=y, color=current_annotation, color_discrete_sequence=discrete_colors[discrete_color_names.index(discrete)], opacity=opacity)
            graph = go.Figure(pxgraph.to_dict())

            graph.update_traces(legendgroup=current_name, legendgrouptitle_text=current_name, marker={'size': dot_size})
            fig.add_traces(graph.data, rows=row, cols=col)
    
    for trace in fig.data:
            if trace.name.lower() == 'yes':
                trace.marker.color = '#3FEB69'
            elif trace.name.lower() == 'no':
                trace.marker.color = '#E02F39'
            elif trace.name.lower() == 'unknown' or trace.name.lower() == 'na':
                trace.marker.color = '#D3D3D3'

    return fig.update_layout(coloraxis={'colorscale': continuous}, legend=dict(groupclick="toggleitem"))

#Functions to check if a string is a float
def isfloat(string):
    try:
        float(string)
        return True
    except:
        return False

#Define our server
server = app.server

#Run our application
if __name__ == '__main__':
    app.run_server(debug=True)