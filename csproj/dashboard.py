from dash import Dash, html, dcc, Input, Output

import pandas as pd 
import plotly.graph_objects as go
import yfinance as yf
from datetime import date



global date_start
date_start='1980-4-17'
global date_end
date_end=date.today
#gets list of all stock tickers
ticks =  pd.read_csv(r'Tickers.csv')
ticker_List = ticks['Ticker'].tolist()
company_Name = ticks['Name'].tolist()
option = [{'label': t, 'value': t} for t in ticker_List]

#fetches OHLC data for a given ticker
def stock_data(stock_ticker):
    stock = yf.Ticker(stock_ticker)
    df = stock.history(interval='1d', start = date_start, end=date_end)
    global open_data 
    open_data = df['Open'].tolist()
    global high_data 
    high_data = df['High'].tolist()
    global low_data 
    low_data = df['Low'].tolist()
    global close_data  
    close_data = df['Close'].tolist()
    global dates 
    dates =df.index

def line_chart(find_ticker):
    stock_data(find_ticker)
    fig = go.Figure([go.Scatter(x=dates, y=close_data)])
    return fig

#generates chart
def OHLC_chart(find_ticker):
    stock_data(find_ticker)
    fig = go.Figure(data=[go.Candlestick(x=dates,
                        open=open_data, high=high_data,
                        low=low_data, close=close_data)]
                        )
    return fig


# visit http://127.0.0.1:8050/ in your web browser.

app = Dash(__name__)


app.layout = html.Div(
    children=[
    

    dcc.Dropdown(options=option,value="GOOG",id="dropdown"),




    html.Div(

    dcc.Loading
    (
            id="loading-icon", className="dash-spinner",
            children=[         
            dcc.RadioItems(
            options=[
            {'label': 'Line', 'value': 'line'},
            {'label': 'candlestick', 'value': 'candle'},
            ],
            value='line',
            id = 'radio'
            ),
            dcc.DatePickerRange(
            id='date-picker-range',
            min_date_allowed=date(1980, 3, 17),
            max_date_allowed=date.today(),
            initial_visible_month=date(2022, 12, 1),
            end_date=date.today(),
            display_format='DD/MM/YY',
            ),
            html.Div(
            dcc.Graph(id = 'chart_plot')
            )
            ],
            type="default",
     style={'left':'1px'})
    )

])
    
@app.callback(
    Output('chart_plot','figure'),
    Input('radio','value'),
    Input('dropdown','value'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date'))
def update_graph(radio_val,input_value,start_date,end_date):
    if input_value is None:
        figure = line_chart('APC')
        figure.layout.plot_bgcolor = '#2A3042'
        figure.layout.paper_bgcolor = '#2A3042'
        figure.layout.font= {"color": "white"}

        figure.update_yaxes(gridwidth=1, gridcolor='#36393f')
        figure.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=True))
        return figure
    else:
        if start_date is not None:
            global date_start
            date_start = start_date
        if end_date is not None:
            global date_end
            date_end = end_date
        if radio_val == 'candle':
            figure = OHLC_chart(input_value)
        if radio_val == 'line':
            figure = line_chart(input_value)
        
        figure.layout.plot_bgcolor = '#2A3042'
        figure.layout.paper_bgcolor = '#2A3042'
        figure.layout.font= {"color": "white"}

        figure.update_yaxes(gridwidth=1, gridcolor='#36393f')
        figure.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=True))
        return figure
    



if __name__ == '__main__':
    app.run_server(debug=True)


