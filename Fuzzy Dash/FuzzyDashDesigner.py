import dash
import dash_cytoscape as cyto
import dash_html_components as html
#import dash_daq as daq


urlz= 'img/Capture.png'
app = dash.Dash(__name__)
app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-compound',
        layout={'name': 'grid','rows':'4', 'colums':'5'},
        style={'width': '100%', 'height': '450px', 'minzoom':'20%','shape':'rectangle'},

        elements=[

          {
                'data': {'id': 'invar', 'label': 'Input Variable 1'},
                
            },
             #Consequent
            {
                'data': {'id': 'outvar1', 'label': 'Output Variable 1'},
                #'position': {'x': -100, 'y': 0}
            },
           
            {
                'data': {'id': 'invar2', 'label': 'Input Variable 2'},
                #'position': {'x': -100, 'y': 50}
            },            
    

            {        
                'data': {'id': 'rule', 'label': 'Rules'},
                #'position': {'x': 250, 'y': 100}
            },

            {
                'data': {'id': 'invar1', 'label': 'Input Variable 3'},
               # 'position': {'x': 400, 'y': 100}
            },
        # Edges
            {

                'data': {'source': 'invar', 'target': 'rule'},
                'classes': 'cities'
            },
            {

                'data': {'source': 'invar1', 'target': 'rule'},
                'classes': 'cities'
            },
            {
                'data': {'source': 'invar2', 'target': 'rule'},
                'classes': 'cities'
            },
            {
                'data': {'source': 'rule', 'target': 'outvar1'},
                'classes': 'cities'
            }
        ],
                stylesheet=[
            {
                'selector': 'node',
                'style': {
                'shape':'rectangle',
                'background-fit': 'cover',
                'background-image':'urlz'},
                
            },
            {
                'selector': '.countries',
                'style': {'width': 5},
                'Background-image':'Capture.PNG'
            },
            {
                'selector': '.node',
                'style': {'line-style': 'solid', 'shape':'circle',
                'Background-image':'Capture.PNG'
                }
            }
        ]



    ),

])

if __name__ == '__main__':
    app.run_server(debug= True, port=8080)