import dash
import dash_cytoscape as cyto
import dash_html_components as html
#import dash_daq as daq
app = dash.Dash(__name__)
app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-compound',
        layout={'name': 'grid','rows':'1', 'colums':'3'},
        style={'width': '100%', 'height': '450px', 'minzoom':'20%','shape':'rectangle'},
        stylesheet=[
            {
                'selector': 'node',
                'style': {'content': 'data(label)'},
                'shape':'rectangle'
            },
            {
                'selector': '.countries',
                'style': {'width': 5, 'shape':'rectangle'}
            },
            {
                'selector': '.cities',
                'style': {'line-style': 'solid', 'shape':'rectangle'}
            }
        ],
        elements=[
 # 1st Gen Parent Nodes 
            {
                'data': {'id': 'at', 'label': 'Antecedents_1'}
            },
            {
                'data': {'id': 'fie', 'label': 'Fuzzy Inference Engine_1'}
            },
            {
                'data': {'id': 'cn', 'label': 'Consequents_1'}
            },
# Nested [2nd Gen] Parents and Children Nodes [clickable to show and edit membership functions in Callback pane]   
        #Antecendents
            {
                'data': {'id': 'gp1', 'label': 'Group Variables X', 'parent': 'at'},
                
            },
            {
                'data': {'id': 'gpinvar1', 'label': 'Grouped Input Variable 1', 'parent': 'gp1'},
                #'position': {'x': -100, 'y': 0}
            },
                        {
                'data': {'id': 'gpinvar2', 'label': 'Grouped Input Variable 2', 'parent': 'gp1'},
                #'position': {'x': -100, 'y': 50}
            },            
            {
                'data': {'id': 'invar2', 'label': 'Input Variable 2', 'parent': 'at'},
                #'position': {'x': -100, 'y': 100}
            },
        #Fuzzy Inference Engine
            {        
                'data': {'id': 'PCA', 'label': 'PCA', 'parent': 'fie'},
                #'position': {'x': 150, 'y': 100}
            },

             {        
                'data': {'id': 'nrm', 'label': 'Normalized1', 'parent': 'fie'},
                #'position': {'x': 175, 'y': 100}
            },

            {        
                'data': {'id': 'rule', 'label': 'Rules', 'parent': 'fie'},
                #'position': {'x': 250, 'y': 100}
            },
        #Consequents
            {
                'data': {'id': 'outvar1', 'label': 'Output Variable 1', 'parent': 'cn'},
               # 'position': {'x': 400, 'y': 100}
            },
        # Edges
            {

                'data': {'source': 'gpinvar1', 'target': 'fie'},
                'classes': 'cities'
            },
            {

                'data': {'source': 'gpinvar2', 'target': 'fie'},
                'classes': 'cities'
            },
            {
                'data': {'source': 'invar2', 'target': 'fie'},
                'classes': 'cities'
            },
            {
                'data': {'source': 'fie', 'target': 'cn'},
                'classes': 'cities'
            }
        ]
    ),

])

if __name__ == '__main__':
    app.run_server(debug= True, port=8080)