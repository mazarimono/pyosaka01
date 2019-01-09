import dash  
import dash_core_components as dcc  
import dash_html_components as html
import plotly.graph_objs as go  
import pandas as pd 
import base64 
import os   

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([
    html.Div([
        #tabs
        html.Div([
            dcc.Tabs(
                id="tabs",
                style=tabs_styles,
                children = [
                    dcc.Tab(label="Front-Page", value="frontpage", style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label="Self-Introduce", value="introduce", style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label="Blockchain-Kyoto", value="bckyoto", style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label='hannari-Python', value='hanpy', style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label="Page-1", value="page1", style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label="Page-2", value="page2", style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label="Page-3", value="page3", style=tab_style, selected_style=tab_selected_style)
                ],
                value="frontpage"
            )
        ],
        className="tab_div"), 
        html.Div(id="tabs-contents")   
    ])
])

@app.callback(dash.dependencies.Output('tabs-contents', 'children'),
            [dash.dependencies.Input("tabs", 'value')])
def render_content(tab):
    if tab == "frontpage":
        return html.Div([
            html.Div([
            html.H1("Dashを使ってプレゼン資料を作る")], style={'color': 'blue', 'fontSize': 50}),
            html.Div([
            html.P("PyOsaka 2019/01/09")], style={'color': 'skyblue', 'marginTop': '5%', 'fontSize': 40}),
            html.Div([
            html.P("合同会社長目　小川　英幸")], style={'color': 'green', 'marginTop': '5%', 'fontSize': 50})
        ], style={'marginTop': '15%', 'textAlign': 'center'})
    elif tab == "introduce":
        return html.Div([
            html.H1("Who am I"),
            html.Div([
            html.H3("小川　英幸(@OgawaHideyuki)")], style={'marginTop': '3%'}),
            html.Div([
            html.H3("はんなりPython,BlockchainKyotoのオーガナイザー")], style={'marginTop': '3%'}),
            html.Div([
            html.H3("プログラミング歴　3年　==  Python歴")],style={'marginTop': '3%'}),
            html.Div([
            html.H3("2つめの言語としてJavaScript勉強中")],style={'marginTop': '3%'})
        ], style={'marginTop': '10%', 'textAlign': 'center'})
    elif tab == "bckyoto":
        return html.Div([
            html.H1("Blockchain Kyoto 2019/1/13 IOST MeetUp"),
            html.H1("JavaScriptでスマートコントラクトを作ろう！"),
            html.Img(src= "https://cdn-ak.f.st-hatena.com/images/fotolife/m/mazarimono/20190107/20190107132618.png"),
            html.Div([
            html.H4(
            "通常会も1月23日に開催　connpassはhttps://blockchain-kyoto.connpass.com/event/114802/")
            ], style={'marginTop': '4%'}),
            #ローカルの画像の埋め込みができない。サードパーティーに入れていると出きるみたいだけど
        ], style={'marginTop': '5%', 'textAlign': 'center'})
    elif tab == "hanpy":
        return html.Div([
            html.H1("はんなりPythonの会#13　2019年1月18日金曜日"),
            html.H3('Dash Hands On Returns'),
            html.Img(src="https://cdn-ak.f.st-hatena.com/images/fotolife/m/mazarimono/20190107/20190107172847.png"),
            html.H3('11月の1回目はPydata Osakaのブログで取り上げてもらいました！  https://bit.ly/2TBXlgl')
        ], style={'marginTop': '5%', 'textAlign': 'center'})
    elif tab == "page1":
        return html.Div([
            html.Div([
            html.H1("Dash： 可視化ツール")], style={'marginTop': '3%', "marginLeft": '5%'}),
            html.Div([
            html.H3("/ FlaskとReactJSとPlotlyJSを使ってウェブアプリケーションを作るライブラリ")], style={'marginTop': '3%', "marginLeft": '5%'}),
            html.Div(style={"backgroundColor": colors['background']}, children=[
                html.H1(
                    children="Hello Dash",
                    style={
                        'textAlign': 'center',
                        'color': colors['text'],
                        'marginTop': '3%'
                    }
                ),
                html.Div(children="Dash: A web application framework for Python.", style={
                    'textAlign': 'center',
                    'color': colors['text']
                }),

                dcc.Graph(
                    id = 'first-graph',
                    figure = {
                    'data' : [
                        {'x': [1, 2, 3, 4, 5], 'y':[4, 5, 6, 3, 2], 'type':'bar', 'name': 'TOkyo'},
                        {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3,4, 5], 'type': 'bar', 'name': 'Osaka'},
                        {'x': [1, 3,4,5], 'y': [1, 1, 3,6 ], 'type': 'bar', 'name': 'Kyoto'}
                    ],
                    'layout' :{
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font': {
                            'color': colors['text']
                        }
                    }
                    } 
                )
            ]),
            html.Div([
                html.H3("/ 見難いものも見やすくできる！")
            ], style={'marginTop': '3%', 'marginLeft': '5%'}),
            html.Div([
                dcc.Graph(
                    id='second-graph',
                    figure = {
                        'data':[
                        {'x': [1, 2, 3, 4, 5], 'y':[4, 5, 6, 3, 2], 'type':'line', 'name': 'TOkyo'},
                        {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3,4, 5], 'type': 'line', 'name': 'Osaka'},
                        {'x': [1, 3,4,5], 'y': [1, 1, 3,6 ], 'type': 'line', 'name': 'Kyoto'} ,
                        {'x': [1, 2, 3, 4, 5], 'y':[3, 5, 4, 3, 1], 'type': 'line', 'name': 'mie'},
                        {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 3, 6, 4], 'type': 'line', 'name': 'wakayama'},
                        {'x': [1, 2, 3, 4, 5], 'y': [4, 3, 4, 2, 1], 'type': 'line', 'name': 'shiga'} ,
                        {'x': [1, 2, 3, 4, 5], 'y':[2, 4, 1, 3, 4], 'type': 'line', 'name': 'nara'},
                        {'x': [1, 2, 3, 4, 5], 'y': [5, 4, 3, 4, 3], 'type': 'line', 'name': 'hyogo'}                          
                        ],
                    'layout': {
                        'height': 600
                    }
                    }
                )
            ], style={'marginBottom': '5%'})
        ])
    elif tab == 'page2':

    else:
        pass

if __name__ == "__main__":
    app.run_server(debug=True)    