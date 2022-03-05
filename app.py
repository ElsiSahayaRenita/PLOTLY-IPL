import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
USERNAME_PASSWORD_PAIRS=[['ipl','ipl']]
app=dash.Dash(__name__)
auth= dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
server=app.server
df = pd.read_csv('https://raw.githubusercontent.com/srinathkr07/IPL-Data-Analysis/master/matches.csv')
df.drop(['id','dl_applied', 'umpire3'], axis =1)
df =df.fillna(0)
que1 = go.Figure(data=[go.Pie(labels=df.winner, values=df.season, pull=[0, 0, 0.5, 0], title="BEST TEAM BASED ON WINNING COUNT")])
que2 = px.line(df, x="season", y="player_of_match", color="date", markers=True,title='BEST PLAYER BASED ON PLAYER OF MATCH')
que3= make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
que3.add_trace(go.Pie(labels=df.winner, values=df.win_by_runs, name="WIN BY RUNS"),
              1, 1)
que3.add_trace(go.Pie(labels=df.winner, values=df.win_by_wickets, name="WIN BY WICKETS"),
              1, 2)
que3.update_traces(hole=.5, hoverinfo="label+percent+name")
que3.update_layout(
    title_text="BEST TEAM BASED ON THE WIN BY RUNS AND WIN BY WICKETS",
    annotations=[dict(text='RUNS', x=0.19, y=0.5, font_size=25, showarrow=False),
                 dict(text='WICKETS', x=0.83, y=0.5, font_size=25, showarrow=False)])
que4 = px.bar(df, x="venue",  color="winner", title="LUCKIEST VENUE FOR EACH TEAM", barmode='relative')
que4.update_traces(marker_color='rgb(198,202,225)', marker_line_color='rgb(200,18,07)', marker_line_width=2, opacity=0.8)
que5 = px.bar(df, x="winner", y="toss_winner", color="toss_winner", title="PROBABILITY OF WINNING MATCH VS WINNING TOSS", barmode='group')

app.layout = html.Div([html.H1(children='ANALYSIS OF INDIAN PREMIER LEAGUE IPL dataset',style={'textalign':'center','color':'black','backgroundcolor':'white'}),
   html.Div([
             dcc.Graph(
       id='example-graph1',
       figure=que1
   ),
   dcc.Graph(
       id='example-graph-2',
       figure=que2
   ),
   dcc.Graph(
       id='example-graph-3',
       figure=que3
   ),
   dcc.Graph(
       id='example-graph-4',
       figure=que4
   ),
   dcc.Graph(
       id='example-graph-5',
       figure=que5
   )
])
])
if __name__ == '__main__':
    app.run_server(debug='True')
