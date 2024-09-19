import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('automobile_sales_dataset.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("XYZAutomotives Sales Dashboard"),
    dcc.Dropdown(
        id='vehicle-type-dropdown',
        options=[{'label': v, 'value': v} for v in df['Vehicle_Type'].unique()],
        multi=True,
        placeholder="Select Vehicle Types"
    ),
    dcc.Graph(id='sales-trend-graph')
])


@app.callback(
    Output('sales-trend-graph', 'figure'),
    [Input('vehicle-type-dropdown', 'value')]
)
def update_graph(selected_vehicle_types):
    filtered_df = df if not selected_vehicle_types else df[df['Vehicle_Type'].isin(selected_vehicle_types)]
    fig = px.line(filtered_df, x='Year', y='Automobile_Sales', color='Vehicle_Type', title="Sales Trend by Vehicle Type")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
