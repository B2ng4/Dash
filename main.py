import dash
from dash import html
from dash import dcc
from dash import dash_table
from dash import html
from dash import dcc
import plotly.graph_objs as go
import pandas as pd

# Данные
labels = ['Категория 1', 'Категория 2', 'Категория 3', 'Категория 4', 'Категория 5']
values = [35, 20, 15, 22, 12]

data = {'date': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01'],
        'value': [10, 20, 30, 25, 35]}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])

# Создаем Dash приложение
app = dash.Dash(__name__)

# Определяем макет приложения
app.layout = html.Div([
    html.H1('Линейный график'),
    dcc.Graph(
        figure={
            'data': [
                go.Scatter(x=df['date'], y=df['value'], mode='lines+markers', name='Временной ряд')
            ],
            'layout': {
                'title': 'График расходов и доходов',
                'xaxis': {'title': 'Месяц'},
                'yaxis': {'title': 'Сумма'}
            }
        }
    ),
    
    dcc.Graph(
        figure={
            'data': [go.Pie(labels=labels, values=values)],
            'layout': {
                'title': 'Круговая диаграмма'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)