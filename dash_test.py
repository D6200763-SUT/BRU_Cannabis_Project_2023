# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

df_cb = pd.read_csv('dataset_CB_10-04-2023.csv',index_col=0)
# df_cb = pd.read_csv('dataset_CB_09-04-2023.csv')

colum_list = list(df_cb)

df_time = df_cb.loc['2023-04-08 00-00-00':'2023-04-09 23-59-00']
df_time.head()

fig1 = px.line(df_time,x=df_time.index, y=df_cb.columns[1:11],title='Air-Temperatures')
# fig1.show()


fig2 = px.line(df_time,x=df_time.index, y=df_cb.columns[11:21],title='Air-Humidity')
# fig2.show()

fig3 = px.line(df_time,x=df_time.index, y=df_cb.columns[21:25],title='Soil-Temperatures')
# fig3.show()

fig4 = px.line(df_time,x=df_time.index, y=df_cb.columns[25:29],title='Soil-Humidity')
# fig4.show()

fig5 = px.line(df_time,x=df_time.index, y=df_cb.columns[29:33],title='Soil-EC')
# fig5.show()

fig5 = px.line(df_time,x=df_time.index, y=df_cb.columns[33:37],title='Soil-PH')
# fig5.show()

fig6 = px.line(df_time,x=df_time.index, y=df_cb.columns[37:41],title='light-Lux')
# fig6.show()

fig7 = px.line(df_time,x=df_time.index, y=df_cb.columns[41:43],title='Co2-ppm')
# fig7.show()






# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig1,

       
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
