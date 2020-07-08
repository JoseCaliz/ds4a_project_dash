import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from server import app
from templates.includes.generate_template import full_template
import pandas as pd
import plotly.express as px
from server import db
import plotly.graph_objects as go


template = full_template
app.title = 'bla'

# template = template.replace('{home_div}', '')
# template = template.replace('{dashboard_div}', 'active')
# template = template.replace('{models_div}', '')
# template = template.replace('{tables_div}', '')
# template = template.replace('{about_div}', '')
# template = template.replace('{info_div}', '')

# app.index_string = template

engine = db.engine

hidden_div = html.Div(className='current_location',
                      children='home',
                      hidden=True)

hidden_div = html.Div(className='current_location',
                      children='home',
                      hidden=True)

layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    html.Div(children='''
        Dash: A web application framework for Python.
    ''')
])

# queries_year ='''
# SELECT extract(year FROM fecha) AS año,
    # COUNT(departamento) AS cantidad,
    # 'hurto automotores' AS crimen
# FROM hurto_automotores
# GROUP BY año
# ---
# SELECT extract(year FROM fecha) AS año,
    # COUNT(departamento) AS cantidad,
    # 'hurto personas'AS crimen
# FROM hurto_personas
# GROUP BY año
# ---
# SELECT extract(year FROM fecha) AS año,
    # COUNT(departamento) AS cantidad,
    # 'violencia intrafamiliar'AS crimen
# FROM violencia_intrafamiliar
# GROUP BY año
# ---
# SELECT extract(year FROM fecha) AS año,
    # COUNT(departamento) AS cantidad,
    # 'delitos sexuales'AS crimen
# FROM del_sexuales
# GROUP BY año
# ---
# SELECT extract(year FROM fecha) AS año,
    # COUNT(departamento) AS cantidad,
    # 'lesiones personales'AS crimen
# FROM lesiones_personales
# GROUP BY año
# ---
# SELECT extract(year FROM fecha) AS año,
    # COUNT(departamento) AS cantidad,
    # 'homicidios'AS crimen
# FROM homicidios
# GROUP BY año
# ---
# SELECT extract(year FROM fecha) AS año,
    # COUNT(departamento) AS cantidad,
    # 'hurto motocicletas'AS crimen
# FROM hurto_motocicletas
# GROUP BY año
# '''.split("---")

# df = pd.concat([pd.read_sql_query(q, engine.connect()) for q in queries_year])\
    # .reset_index(drop=True).sort_values('año')


# fig = go.Figure()
# fig.add_trace(
    # go.Scatter(x=list(df[df.crimen=='hurto automotores'].año),
               # y=list(df[df.crimen=='hurto automotores'].cantidad),
               # name="Car theft",
               # line=dict(color=px.colors.qualitative.Plotly[0])))

# fig.add_trace(
    # go.Scatter(x=list(df[df.crimen=='hurto personas'].año),
               # y=list(df[df.crimen=='hurto personas'].cantidad),
               # name="Shoplifting",
               # line=dict(color=px.colors.qualitative.Plotly[1])))

# fig.add_trace(
    # go.Scatter(x=list(df[df.crimen=='violencia intrafamiliar'].año),
               # y=list(df[df.crimen=='violencia intrafamiliar'].cantidad),
               # name="Violencia intrafamiliar",
               # line=dict(color=px.colors.qualitative.Plotly[2])))

# fig.add_trace(
    # go.Scatter(x=list(df[df.crimen=='delitos sexuales'].año),
               # y=list(df[df.crimen=='delitos sexuales'].cantidad),
               # name="Sexual crimes",
               # line=dict(color=px.colors.qualitative.Plotly[3])))

# fig.add_trace(
    # go.Scatter(x=list(df[df.crimen=='lesiones personales'].año),
               # y=list(df[df.crimen=='lesiones personales'].cantidad),
               # name="Personal injuries",
               # line=dict(color=px.colors.qualitative.Plotly[4])))

# fig.add_trace(
    # go.Scatter(x=list(df[df.crimen=='homicidios'].año),
               # y=list(df[df.crimen=='homicidios'].cantidad),
               # name="Murders",
               # line=dict(color=px.colors.qualitative.Plotly[5])))

# fig.add_trace(
    # go.Scatter(x=list(df[df.crimen=='hurto motocicletas'].año),
               # y=list(df[df.crimen=='hurto motocicletas'].cantidad),
               # name="Theft of motorcycles",
               # line=dict(color=px.colors.qualitative.Plotly[6])))

# fig.update_layout(
    # updatemenus=[
        # dict(
            # active=0,
            # buttons=list([
                # dict(label="All",
                     # method="update",
                     # args=[{"visible": [True, True, True, True, True, True, True]},
                           # {"title": "Crimes in Colombia"}]),
                # dict(label="Car theft",
                     # method="update",
                     # args=[{"visible": [True, False, False, False, False, False, False]},
                           # {"title": "Car theft in Colombia"}]),
                # dict(label="Shoplifting",
                     # method="update",
                     # args=[{"visible": [False, True, False, False, False, False, False]},
                           # {"title": "Shoplifting in Colombia"}]),
                # dict(label="Domestic violence",
                     # method="update",
                     # args=[{"visible": [False, False, True, False, False, False, False]},
                           # {"title": "Domestic violence in Colombia"}]),
                # dict(label="Sexual crimes",
                     # method="update",
                     # args=[{"visible": [False, False, False, True, False, False, False]},
                           # {"title": "Delitos sexuales in Colombia"}]),
                # dict(label="Personal injuries",
                     # method="update",
                     # args=[{"visible": [False, False, False, False, True, False, False]},
                           # {"title": "Personal injuries in Colombia"}]),
                # dict(label="Murders",
                     # method="update",
                     # args=[{"visible": [False, False, False, False, False, True, False]},
                           # {"title": "Murders in Colombia"}]),
                # dict(label="Theft of motorcycles",
                     # method="update",
                     # args=[{"visible": [False, False, False, False, False, False, True]},
                           # {"title": "Theft of motorcycles in Colombia"}])
            # ]),
        # )
    # ])

# fig.update_layout(title_text="Crimes in Colombia")
# graph_1 = dcc.Graph(
    # id='all_problems-graph',
    # figure = fig
# )

# # -----------------------------------------------
# query_homicidios = '''
# SELECT
    # date_part('year', fecha) as fecha,
    # sexo,
    # 'Homicidios' as crime,
    # count(*)
# FROM del_sexuales
# WHERE
    # sexo != 'NO REPORTA'
    # AND sexo != 'NO REPORTADA'
    # AND sexo != 'NO REPORTADO'
# group by 1,2,3
# UNION ALL
# SELECT
    # date_part('year', fecha) as fecha,
    # sexo,
    # 'Hurto Motocicletas' as crime,
    # count(*)
# FROM hurto_motocicletas
# WHERE
    # sexo != 'NO REPORTA'
    # AND sexo != 'NO REPORTADA'
    # AND sexo != 'NO REPORTADO'
# group by 1,2,3
# UNION ALL
# SELECT
    # date_part('year', fecha) as fecha,
    # sexo,
    # 'Hurto Automotores' as crime,
    # count(*)
# FROM hurto_automotores
# WHERE
    # sexo != 'NO REPORTA'
    # AND sexo != 'NO REPORTADA'
    # AND sexo != 'NO REPORTADO'
# group by 1,2,3
# UNION ALL
# SELECT
    # date_part('year', fecha) as fecha,
    # sexo,
    # 'Hurto Personas' as crime,
    # count(*)
# FROM hurto_personas
# WHERE
    # sexo != 'NO REPORTA'
    # AND sexo != 'NO REPORTADA'
    # AND sexo != 'NO REPORTADO'
# group by 1,2,3
# UNION ALL
# SELECT
    # date_part('year', fecha) as fecha,
    # sexo,
    # 'Lesiones Personales' as crime,
    # count(*)
# FROM lesiones_personales
# WHERE
    # sexo != 'NO REPORTA'
    # AND sexo != 'NO REPORTADA'
    # AND sexo != 'NO REPORTADO'
# group by 1,2,3
# UNION ALL
# SELECT
    # date_part('year', fecha) as fecha,
    # sexo,
    # 'Domestic Violence' as crime,
    # count(*)
# FROM violencia_intrafamiliar
# WHERE
    # sexo != 'NO REPORTA'
    # AND sexo != 'NO REPORTADA'
    # AND sexo != 'NO REPORTADO'
# group by 1,2,3;
# '''

# df_f = pd.read_sql_query(query_homicidios, engine)

# plot_2 = px.bar(
    # data_frame=df_f,
    # x='fecha',
    # y='count',
    # color='sexo',
    # animation_frame='crime',
# )

# plot_2.update_layout(
    # title='Counts per Year',
    # xaxis=dict(title='Year'),
    # yaxis=dict(title='Counts')
# )

# graph_2 = dcc.Graph(
    # id='conteo_edad',
    # figure=plot_2
# )


# # ---------------------------------

# # queries_yearly ='''
# # SELECT *
# # FROM del_sexuales
# # '''

# # df1 = pd.read_sql_query(queries_yearly, db.engine)

# # print(df1.head())
# # print(df1.columns.to_list())

# # years = df1.fecha.dt.year.unique()
# # years.sort()
# # fig3 = go.Figure()
# # c=0
# # for year in years:
    # # fig3.add_trace(
        # # go.Scatter(x=df1.fecha.reset_index().groupby('date').count().index,
                   # # y=df1[df1.year==year].fecha.reset_index().groupby('date').count().reset_index()['index'],
                   # # name=str(year),
                   # # line=dict(color=px.colors.qualitative.Plotly[c])))
    # # c+=1
# # updatemenu=[]
# # buttons=[]
# # buttons.append(dict(method='restyle',
                        # # label='All',
                        # # args=[{"visible":[True for x in range(len(years))]},
                              # # {"title":'Sex Offenses in CO'}]
                        # # )
                  # # )
# # # button with one option for each dataframe
# # c=0
# # for year in years:
    # # xx=[False for x in range(len(years))]
    # # xx[c]=True
    # # buttons.append(dict(method='restyle',
                        # # label=str(year),
                        # # args=[{"visible":xx},
                              # # {"title":str(year)}]
                        # # )
                  # # )
    # # c+=1
# # updatemenu=[]
# # your_menu=dict()
# # updatemenu.append(your_menu)
# # updatemenu[0]['buttons']=buttons
# # updatemenu[0]['direction']='down'
# # updatemenu[0]['showactive']=True
# # # add dropdown menus to the figure
# # fig3.update_layout(updatemenus=updatemenu)
# # fig3.update_layout(title_text="Crimes in Colombia")

# # graph_3 = dcc.Graph(id='blablabla', figure=fig3)
# # # ---------------------------------



# TABLES_LIST=['hurto_automotores', 'hurto_personas','violencia_intrafamiliar',
             # 'del_sexuales','lesiones_personales','homicidios','hurto_motocicletas']
# TABLES_LIST_NICK=['hurto automotores', 'hurto Personas','violencia intrafamiliar',
             # 'delitos sexuales','lesiones personales','homicidios','hurto motocicletas']
# COLUMN_LIST=['fecha','departamento','hora']

# TITLES=['Car theft in Colombia','Shoplifting in Colombia','Domestic violence in Colombia',
        # 'Sexual crimes in Colombia', 'Personal injuries in Colombia','Murders in Colombia',
        # 'Theft of motorcycles in Colombia']
# LABELS=['Car theft','Shoplifting','Domestic violence','Sexual crimes', 
        # 'Personal injuries','Murders','Theft of motorcycles']
# GEN_GRAPH_TITLE=['Crimes in Colombia By Year','Crimes in Colombia By Hour']



# one_que=[]
# for idx,i in enumerate(TABLES_LIST):
    # a='''SELECT extract(year FROM {col0}) AS año,
            # COUNT({col1}) AS cantidad,
            # '{tabn}' AS crimen
        # FROM {tab}
        # GROUP BY año'''.format(tab=i,tabn=TABLES_LIST_NICK[idx],col0=COLUMN_LIST[0],col1=COLUMN_LIST[1])
    # one_que.append(a)



# ## query por horas
# one_que2=[]
# for idx,i in enumerate(TABLES_LIST):
    # if i == 'del_sexuales' or i == 'lesiones_personales' or i == 'homicidios':
        # pass
    # else:
        # a='''SELECT {col0} AS hora,
                # COUNT({col1}) AS cantidad,
                # '{tabn}' AS crimen
            # FROM {tab}
            # GROUP BY hora'''.format(tab=i,tabn=TABLES_LIST_NICK[idx],col0=COLUMN_LIST[2],col1=COLUMN_LIST[1])
    # one_que2.append(a)


    # #df graph 1
# df_cris = pd.concat([pd.read_sql_query(q, db.engine) for q in one_que])\
    # .reset_index(drop=True).sort_values('año')
# #df graph 2
# ## faltan columnas de hora del_sexuales', 'lesiones_personales','homicidios'
# df2_cris_2 = pd.concat([pd.read_sql_query(q, db.engine) for q in one_que2])\
    # .reset_index(drop=True).sort_values('hora')


# figure_cristian = go.Figure()

# for idx,i in enumerate(TABLES_LIST_NICK):
        # if False: # i == 'delitos sexuales' or i == 'lesiones personales' or i == 'homicidios':
            # pass
        # else:
            # figure_cristian.add_trace(
                # go.Scatter(x=list(df2_cris_2[df2_cris_2.crimen==i].hora),
                           # y=list(df2_cris_2[df2_cris_2.crimen==i].cantidad),
                           # name=LABELS[idx],
                           # line=dict(color=px.colors.qualitative.Plotly[idx])))

# btns=[]
# ## add general title
# btns.append(dict(label="All",
            # method="update",
                # args=[{"visible": [True]*(len(LABELS))},
                  # {"title": GEN_GRAPH_TITLE[1]}]))

# # add titles
# for idx, j in enumerate(TITLES):
    # visible=[False]*(len(LABELS))
    # visible[idx]=True
    # if False: #j == 'Sexual crimes in Colombia' or j == 'Personal injuries in Colombia' or j == 'Murders in Colombia':
        # pass
    # else:
        # btns.append(dict(label=LABELS[idx],
                         # method="update",
                         # args=[{"visible": visible},
                               # {"title": j}]))


# figure_cristian.update_layout(updatemenus=[dict(active=0,buttons=btns)])
# figure_cristian.update_layout(title_text=GEN_GRAPH_TITLE[1])

# graph_4 = dcc.Graph(id='otra', figure=figure_cristian)

# layout = html.Div([
    # graph_1,
    # graph_2,
    # graph_4
# ])
