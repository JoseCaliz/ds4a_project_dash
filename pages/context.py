import dash
import dash_html_components as html

layout = html.Div(children=[

    html.Header(className= 'header fade-in',children=[
        html.Div(className="header__circle header__dot1"),
        html.Div(className="header__circle header__dot2"),
        html.Div(className="header__circle header__dot3"),
        html.Div(className="header__circle header__dot4"),
        html.P("TEAM 79 FOUNDATION",className="header__team"),
        "ANALYZING CRIME TRENDS IN COLOMBIA"
    ]),
    html.Section(className="context",children=[
        html.Div(className="title_co",children=["GENERAL CONTEXT"]),
        
        html.Article(className="context__row",children=[
            html.Div(className="context__col",children=[
                html.Img(src="./assets/images/datafolio/img1t.png")
            ]),
            html.Div(className="context__col",children=[
                html.P(children=[
                    html.Span(className="blue",children=["Crime and violence "]),
                    "are the main concerns of all citizens around the world and generates impacts on our society and exception."
                ])
            ])
        ]),

        html.Article(className="context__row",children=[
            html.Div(className="context__col",children=[
                html.P(children=[
                    html.Span(className="red",children=["Thefts, domestic violence, sexual crimes and personal injuries increased "]),
                    "between 2010 and 2019 while ",
                    html.Span(className="blue",children=["murders decreased."])
                ])
            ]),
            html.Div(className="context__col",children=[
                html.Img(src="./assets/images/datafolio/img2t.png")
            ])
        ]),

        html.Article(className="context__row",children=[
            html.Div(className="context__col",children=[
                 html.Img(src="./assets/images/datafolio/img3t.png")
            ]),
            html.Div(className="context__col",children=[
                html.P("In 2019 in Colombia it was reported:"),
                html.Ul(children=[
                    html.Li(children=[
                        "A ",
                        html.Span(className="blue",children=["theft"]),
                        " every ",
                        html.Span(className="red",children=["2 minutes."]),
                    ]),
                    html.Li(children=[
                        "A ",
                        html.Span(className="blue",children=["domestic violence"]),
                        " case every ",
                        html.Span(className="red",children=["5 minutes."]),
                    ]),
                    html.Li(children=[
                        "A ",
                        html.Span(className="blue",children=["personal injury"]),
                        " case every ",
                        html.Span(className="red",children=["5 minutes."]),
                    ]),
                    html.Li(children=[
                        "A ",
                        html.Span(className="blue",children=["sexual crime"]),
                        " every ",
                        html.Span(className="red",children=["15 minutes."]),
                    ]),
                    html.Li(children=[
                        "A ",
                        html.Span(className="blue",children=["homicide"]),
                        " every ",
                        html.Span(className="red",children=["42 minutes."]),
                    ])
                ])
            ])
        ]),

        html.Hr(className="divider", style={"size":"2px", "color":"black"}),
        html.Div(className="title_co",children=["THEFT, MURDERS AND ROBBERY"]),

        html.Article(className="context__row",children=[
            html.Div(className="context__col",children=[
                html.P("Theft is one of the most worrying crimes due to its exponential increase in the last three years."),

                html.P(children=[
                    html.Span(className="red",children=["Men "]),
                    "were involved in",
                    html.Span(className="red",children=[" 92% "]),
                    "of murders and in",
                    html.Span(className="red",children=[" 82% "]),
                    "of",
                    html.Span(className="red",children=[" theft of cars an motorcycles."])                  
                ])
            ]),

            html.Div(className="context__col",children=[
                html.Img(src="./assets/images/datafolio/img4t.png")
            ])
        ]),

        html.Hr(className="divider", style={"size":"2px", "color":"black"}),
        html.Div(className="title_co",children=["DOMESTIC VIOLENCE AND SEXUAL CRIMES"]),

        html.Article(className="context__row",children=[
            html.Div(className="context__col",children=[
                html.Img(src="./assets/images/datafolio/img5t.png")
            ]),
            html.Div(className="context__col",children=[
                html.P(children=[
                    html.Span(className="red",children=["Women between 20 and 40 "]),
                    "are more ",
                    html.Span(className="blue",children=["susceptible to domestic violence."])                 
                ]),

                html.P(children=[
                    html.Span(className="red",children=["85% "]),
                    "of",
                    html.Span(className="blue",children=[" sexual crimes "]),
                    "and",
                    html.Span(className="red",children=[" 82% "]),
                    "of",
                    html.Span(className="blue",children=[" domestic violence "]),
                    "cases are",
                    html.Span(className="red",children=[" registered by women."])
             
                ])
            ])
        ]),

        html.Hr(className="divider", style={"size":"2px", "color":"black"}),
        html.Div(className="title_co",children=["MAIN CAUSES"]),

        html.Article(className="context__row",children=[
            html.Div(className="context__col",children=[
                html.P(children=[
                    html.Span(className="blue",children=["Illicit drug trafficking, criminal organizations "]),
                    "and the ",
                    html.Span(className="blue",children=["history of violence "]),
                    "in Colombia have a ",
                    html.Span(className="red",children=["high impact in crime"]),
                    ", especially murder rate."
                ])
            ]),
            html.Div(className="context__col",children=[
                html.Img(src="./assets/images/datafolio/img6t.png")
            ])
        ]),      
    ])
])
