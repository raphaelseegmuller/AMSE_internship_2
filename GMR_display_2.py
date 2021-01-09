import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

from libs import function

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

### Figure ###


app.layout = html.Div(children=[
    dcc.Graph(
        id='graph',
        figure=function.get_GMR_fig_2(["Bouches-du-Rhône"], ['RAR', 'GAP', 'PAR', 'TAS', 'WOR', 'RES'], 'No')
    ),
    html.Div(id='R_value', style={'margin-top': 20}),
    dcc.Dropdown(
        id='R_choice',
        options=[
            {'label': 'France', 'value': 'France'},
            {'label': 'Auvergne-Rhône-Alpes', 'value': 'Auvergne-Rhône-Alpes'},
            {'label': 'Bourgogne-Franche-Comté', 'value': 'Bourgogne-Franche-Comté'},
            {'label': 'Brittany', 'value': 'Brittany'},
            {'label': 'Corsica', 'value': 'Corsica'},
            {'label': 'Centre-Val de Loire', 'value': 'Centre-Val de Loire'},
            {'label': 'Grand Est', 'value': 'Grand Est'},
            {'label': 'Hauts de France', 'value': 'Hauts de France'},
            {'label': 'Ile de France', 'value': 'Ile de France'},
            {'label': 'Nouvelle Aquitaine', 'value': 'Nouvelle Aquitaine'},
            {'label': 'Normandy', 'value': 'Normandy'},
            {'label': 'Occitanie', 'value': 'Occitanie'},
            {'label': 'Pays de la Loire', 'value': 'Pays de la Loire'},
            {'label': 'Provence-Alpes-Côte d\'Azur', 'value': 'Provence-Alpes-Côte d\'Azur'},
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
            {'label': 'Val-d\'Oise', 'value': 'Val - d\'Oise'}
        ],
        value=["Bouches-du-Rhône"],
        multi=True
    ),
    html.Div(id='GMR_selection', style={'margin-top': 20}),
    dcc.Dropdown(
        id='GMR_choice',
        options=[
            {'label': 'RAR', 'value': 'RAR'},
            {'label': 'GAP', 'value': 'GAP'},
            {'label': 'PAR', 'value': 'PAR'},
            {'label': 'TAS', 'value': 'TAS'},
            {'label': 'WOR', 'value': 'WOR'},
            {'label': 'RES', 'value': 'RES'}
        ],
        value=['RAR', 'GAP', 'PAR', 'TAS', 'WOR', 'RES'],
        multi=True
    ),
    html.Div(id='moving_average', style={'margin-top': 20}),
    dcc.Dropdown(
        id='average_choice',
        options=[
            {'label': 'Yes', 'value': 'Yes'},
            {'label': 'No', 'value': 'No'}
        ],
        value='No'
    )
])


### Update figure ###

@app.callback(Output('R_value', 'children'),
              [Input('R_choice', 'value')])
def department(name):
    return 'Department, Region or Country : '


@app.callback(Output('GMR_selection', 'children'),
              [Input('GMR_choice', 'value')])
def GMR_selection(selection_list):
    return 'GMR selection : '


@app.callback(Output('moving_average', 'children'),
              [Input('average_choice', 'value')])
def average_choice(ans):
    return 'Moving average : '


@app.callback(
    Output('graph', 'figure'),
    [Input('R_choice', 'value'),
     Input('GMR_choice', 'value'),
     Input('average_choice', 'value')
     ])
def update_graph(name_list, selection_list, mov_av):
    return function.get_GMR_fig_2(name_list, selection_list, mov_av)


if __name__ == '__main__':
    app.run_server(debug=True)
