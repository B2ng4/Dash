import dash
from dash import html
from dash import dcc
from dash import dash_table
from dash import html
from dash import dcc
import plotly.graph_objs as go
import dash
from dash import html
from dash import dcc
import pandas as pd
from dash.dash_table.Format import Group
import dash
import plotly.express as px
import pandas as pd


df = pd.read_csv('Data_Base/Data.csv')
fig = px.scatter(df, x='profit', y='assets', color='investments', title='Profit vs Assets Scatter Plot')

periods = [
    {'label': 'Месяц', 'value': 'Месяц'},
    {'label': 'Квартал', 'value': 'Квартал'},
    {'label': 'Год', 'value': 'Год'}
]

# Создаем данные для таблицы
data = {'Показатель': ['Общее прибыль', 'Чистый профит', 'Реальная прибыль', 'Проfit/ОТМ'],
        'Значение': [100000, 50000, 30000, 15]}
df = pd.DataFrame(data)

# Создаем данные для круговой диаграммы
labels = ['Категория 1', 'Категория 2', 'Категория 3', 'Категория 4', 'Категория 5']
values = [35, 20, 15, 22, 12]

# Создаем данные для линейного графика
line_data = {'date': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01'],
        'value': [10, 20, 30, 25, 35]}
line_df = pd.DataFrame(line_data)
line_df['date'] = pd.to_datetime(line_df['date'])

# Создаем Dash приложение
app = dash.Dash(__name__)

# Определяем макет приложения
app.layout = html.Div([
    html.H1('Финансовые показатели'),
    dcc.Graph(
        figure={
            'data': [
                {'x': line_df['date'], 'y': line_df['value'], 'type': 'scatter', 'mode': 'lines+markers', 'name': 'Временной ряд'}
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
    ),
    html.Div([
        html.H1('Таблица с данными'),
        dash_table.DataTable(
            columns=[{'id': 'Показатель', 'name': 'Показатель'}, {'id': 'Значение', 'name': 'Значение'}],
            data=df.to_dict('records'),
            style_table={'border': '1px solid black'},
            style_header={'backgroundColor': 'rgb(20, 20, 20)', 'color': 'white'},
            style_cell={'textAlign': 'center', 'backgroundColor': 'rgb(50, 50, 50)', 'color': 'white'}
        )
    ]),
    html.Div([
        dcc.Graph(figure=fig)
]),
    html.Div([
        html.Label('Выберите период анализа:'),
        dcc.Dropdown(
            id='period-dropdown',
            options=periods,
            value='month'  # Значение по умолчанию
        ),
        html.Div(id='output-container')  # Элемент для отображения выбранного значения
    ])
])
@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('period-dropdown', 'value')]
)
def update_output(selected_period):
    return f'Выбран период: {selected_period}'
# Запускаем приложение
if __name__ == '__main__':
    app.run_server(debug=True)

