import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from plotly.subplots import make_subplots

import data
from libs import function

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

### Figure ###


name_list = ["Bouches-du-Rhône"]
fig = make_subplots(rows=1, cols=1)
title = "Confirmed cases - COVID 19"
fig.update_layout(
    title={
        'text': title,
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    title_font_size=30,
    xaxis={'title': 'Date (jour/mois)'},
    yaxis={'title': 'Case number'})
for name in name_list:
    fig.add_scatter(
        x=data.time_list,
        y=function.get_covid_case_list(name),
        name="{}".format(name))

app.layout = html.Div(children=[
    dcc.Graph(
        id='graph',
        figure=fig
    ),
    html.Div(id='Department_value', style={'margin-top': 20}),
    dcc.Dropdown(
        id='Department_choice',
        options=[
            {'label': 'Ain', 'value': 'Ain'},
            {'label': 'Aisne', 'value': 'Aisne'},
            {'label': 'Allier', 'value': 'Allier'},
            {'label': 'Alpes-de-Haute-Provence', 'value': 'Alpes-de-Haute-Provence'},
            {'label': 'Hautes-Alpes', 'value': 'Hautes-Alpes'},
            {'label': 'Alpes-Maritimes', 'value': 'Alpes-Maritimes'},
            {'label': 'Ardèche', 'value': 'Ardèche'},
            {'label': 'Ardennes', 'value': 'Ardennes'},
            {'label': 'Ariège', 'value': 'Ariège'},
            {'label': 'Aube', 'value': 'Aube'},
            {'label': 'Aude', 'value': 'Aude'},
            {'label': 'Aveyron', 'value': 'Aveyron'},
            {'label': 'Bouches-du-Rhône', 'value': 'Bouches-du-Rhône'},
            {'label': 'Calvados', 'value': 'Calvados'},
            {'label': 'Cantal', 'value': 'Cantal'},
            {'label': 'Charente', 'value': 'Charente'},
            {'label': 'Charente-Maritime', 'value': 'Charente-Maritime'},
            {'label': 'Cher', 'value': 'Cher'},
            {'label': 'Corrèze', 'value': 'Corrèze'},
            {'label': 'Côte-d\'Or', 'value': 'Côte - d\'Or'},
            {'label': 'Côtes-d\'Armor', 'value': 'Côtes - d\'Armor'},
            {'label': 'Creuse', 'value': 'Creuse'},
            {'label': 'Dordogne', 'value': 'Dordogne'},
            {'label': 'Doubs', 'value': 'Doubs'},
            {'label': 'Drôme', 'value': 'Drôme'},
            {'label': 'Eure', 'value': 'Eure'},
            {'label': 'Eure-et-Loir', 'value': 'Eure-et-Loir'},
            {'label': 'Finistère', 'value': 'Finistère'},
            {'label': 'Corse-du-Sud', 'value': 'Corse-du-Sud'},
            {'label': 'Haute-Corse', 'value': 'Haute-Corse'},
            {'label': 'Gard', 'value': 'Gard'},
            {'label': 'Haute-Garonne', 'value': 'Haute-Garonne'},
            {'label': 'Gers', 'value': 'Gers'},
            {'label': 'Gironde', 'value': 'Gironde'},
            {'label': 'Hérault', 'value': 'Hérault'},
            {'label': 'Ille-et-Vilaine', 'value': 'Ille-et-Vilaine'},
            {'label': 'Indre', 'value': 'Indre'},
            {'label': 'Indre-et-Loire', 'value': 'Indre-et-Loire'},
            {'label': 'Isère', 'value': 'Isère'},
            {'label': 'Jura', 'value': 'Jura'},
            {'label': 'Landes', 'value': 'Landes'},
            {'label': 'Loir-et-Cher', 'value': 'Loir-et-Cher'},
            {'label': 'Loire', 'value': 'Loire'},
            {'label': 'Haute-Loire', 'value': 'Haute-Loire'},
            {'label': 'Loire-Atlantique', 'value': 'Loire-Atlantique'},
            {'label': 'Loiret', 'value': 'Loiret'},
            {'label': 'Lot', 'value': 'Lot'},
            {'label': 'Lot-et-Garonne', 'value': 'Lot-et-Garonne'},
            {'label': 'Lozère', 'value': 'Lozère'},
            {'label': 'Maine-et-Loire', 'value': 'Maine-et-Loire'},
            {'label': 'Manche', 'value': 'Manche'},
            {'label': 'Marne', 'value': 'Marne'},
            {'label': 'Haute-Marne', 'value': 'Haute-Marne'},
            {'label': 'Mayenne', 'value': 'Mayenne'},
            {'label': 'Meurthe-et-Moselle', 'value': 'Meurthe-et-Moselle'},
            {'label': 'Meuse', 'value': 'Meuse'},
            {'label': 'Morbihan', 'value': 'Morbihan'},
            {'label': 'Moselle', 'value': 'Moselle'},
            {'label': 'Nièvre', 'value': 'Nièvre'},
            {'label': 'Nord', 'value': 'Nord'},
            {'label': 'Oise', 'value': 'Oise'},
            {'label': 'Orne', 'value': 'Orne'},
            {'label': 'Pas-de-Calais', 'value': 'Pas-de-Calais'},
            {'label': 'Puy-de-Dôme', 'value': 'Puy-de-Dôme'},
            {'label': 'Pyrénées-Atlantiques', 'value': 'Pyrénées-Atlantiques'},
            {'label': 'Hautes-Pyrénées', 'value': 'Hautes-Pyrénées'},
            {'label': 'Pyrénées-Orientales', 'value': 'Pyrénées-Orientales'},
            {'label': 'Bas-Rhin', 'value': 'Bas-Rhin'},
            {'label': 'Haut-Rhin', 'value': 'Haut-Rhin'},
            {'label': 'Rhône', 'value': 'Rhône'},
            {'label': 'Haute-Saône', 'value': 'Haute-Saône'},
            {'label': 'Saône-et-Loire', 'value': 'Saône-et-Loire'},
            {'label': 'Sarthe', 'value': 'Sarthe'},
            {'label': 'Savoie', 'value': 'Savoie'},
            {'label': 'Haute-Savoie', 'value': 'Haute-Savoie'},
            {'label': 'Paris', 'value': 'Paris'},
            {'label': 'Seine-Maritime', 'value': 'Seine-Maritime'},
            {'label': 'Seine-et-Marne', 'value': 'Seine-et-Marne'},
            {'label': 'Yvelines', 'value': 'Yvelines'},
            {'label': 'Deux-Sèvres', 'value': 'Deux-Sèvres'},
            {'label': 'Somme', 'value': 'Somme'},
            {'label': 'Tarn', 'value': 'Tarn'},
            {'label': 'Tarn-et-Garonne', 'value': 'Tarn-et-Garonne'},
            {'label': 'Var', 'value': 'Var'},
            {'label': 'Vaucluse', 'value': 'Vaucluse'},
            {'label': 'Vendée', 'value': 'Vendée'},
            {'label': 'Vienne', 'value': 'Vienne'},
            {'label': 'Haute-Vienne', 'value': 'Haute-Vienne'},
            {'label': 'Vosges', 'value': 'Vosges'},
            {'label': 'Yonne', 'value': 'Yonne'},
            {'label': 'Territoire de Belfort', 'value': 'Territoire de Belfort'},
            {'label': 'Essonne', 'value': 'Essonne'},
            {'label': 'Hauts-de-Seine', 'value': 'Hauts-de-Seine'},
            {'label': 'Seine-Saint-Denis', 'value': 'Seine-Saint-Denis'},
            {'label': 'Val-de-Marne', 'value': 'Val-de-Marne'},
            {'label': 'Val-d\'Oise', 'value': 'Val - d\'Oise'},
            {'label': 'Guadeloupe', 'value': 'Guadeloupe'},
            {'label': 'Martinique', 'value': 'Martinique'},
            {'label': 'Guyane', 'value': 'Guyane'},
            {'label': 'Réunion', 'value': 'Réunion'},
            {'label': 'Miquelon-Langlade et Saint Pierre', 'value': 'Miquelon-Langlade et Saint Pierre'},
            {'label': 'Mayotte', 'value': 'Mayotte'},
            {'label': 'Saint-Barthélemy', 'value': 'Saint-Barthélemy'},
            {'label': 'Saint-Martin', 'value': 'Saint-Martin'}
        ],
        value=["Bouches-du-Rhône"],
        multi=True
    )
])


### Update figure ###

@app.callback(Output('Department_value', 'children'),
              [Input('Department_choice', 'value')])
def department(name):
    return 'Department : '


@app.callback(
    Output('graph', 'figure'),
    [Input('Department_choice', 'value')
     ])
def update_graph(name_list):
    new_fig = make_subplots(rows=1, cols=1)
    new_fig.update_layout(
        title={
            'text': title,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        title_font_size=30,
        xaxis={'title': 'Date (jour/mois)'},
        yaxis={'title': 'Case number'})
    for name in name_list:
        new_fig.add_scatter(
            x=data.time_list,
            y=function.get_covid_case_list(name),
            name="{}".format(name))
    return new_fig


if __name__ == '__main__':
    app.run_server(debug=True)
