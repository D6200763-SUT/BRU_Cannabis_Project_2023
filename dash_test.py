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

df_cb = pd.read_csv('dataset_CB_07-04-2023.csv',index_col=0)
# df_cb = pd.read_csv('dataset_CB_05-04-2023.csv')
df_cb.head(5)
colum_list = list(df_cb)

df_airtemp_S_Code1 = df_cb.iloc[:,1:7]
df_airtemp_S_Code2 = df_cb.iloc[:,7:11]
df_airhumid_S_Code1 = df_cb.iloc[:,11:17]
df_airhumid_S_Code2 = df_cb.iloc[:,17:21]

df_soil_temp_S_Code3 = df_cb.iloc[:,21:25]
df_soil_humid_S_Code3 = df_cb.iloc[:,25:29]
df_soil_ec_S_Code3 = df_cb.iloc[:,29:33]
df_soil_ph_S_Code3 = df_cb.iloc[:,33:37]

df_light_S_Code4 = df_cb.iloc[:,37:41]

df_co2_S_Code5 = df_cb.iloc[:,41:43]

fig1 = px.line(df_airtemp_S_Code1,title='Air-Temperatures')
# fig1.show()
fig2 = px.line(df_airhumid_S_Code1,title='Air-Humidity')
# fig2.show()

fig3 = px.line(df_airtemp_S_Code2,title='Air-Temperatures')
# fig3.show()
fig4 = px.line(df_airhumid_S_Code2,title='Air-Humidity')
# fig4.show()






# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig1
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
