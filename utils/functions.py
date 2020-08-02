import joblib as jl
from datetime import datetime
import copy
from fbprophet import Prophet
from pandas import DataFrame, concat, date_range


def highlight_current_page(lev_nav, current_page):
    for key in lev_nav.keys():
        if key == current_page:
            lev_nav[key] = True
        else:
            left_nav[key] = False

    return lev_nav

def predict_time_series(data, crimes):
    data = data.copy()

    prophet_models = [
        'dom_viol',
        'murder'
    ]

    models = jl.load('./models/time_series_models.pkl')
   
    data.rename(columns={'final_sunday':'ds'}, inplace=True)
    data['is_pred'] = False
    for crime in crimes:
        data_temp = data[data.crime == crime].copy()
        if crime in prophet_models:

            # Generate dates Prophet
            dt_predict = DataFrame(
                dict(
                    ds=date_range(
                        start=data_temp.ds.max(),
                        end=datetime.today(),
                        freq='14D'
                    )
                )
            )
            preds = models[crime].predict(dt_predict)

            #removing first column
            preds = preds.iloc[1:, :].rename(
                columns={'yhat':'num_cases'}
            )

            preds['is_pred'] = True
            preds['crime'] = crime 
            #Appending values

            data = concat(
                [data, preds[['ds', 'num_cases', 'is_pred', 'crime']]]
            )
        else:
            date_to_pred = date_range(
                start=data_temp.ds.max(),
                end=datetime.today(),
                freq='14D'
            )[1:]
            
            for i in date_to_pred:
                print(data_temp.iloc[-2:].num_cases)
                pred = models[crime].predict(data_temp.iloc[-3:].num_cases)[0]
                insert = {'ds':i, 'num_cases':pred, 'is_pred':True,
                          'crime':crime}

                data_temp = data_temp.append(insert, ignore_index=True)

            data = concat(
                [data, data_temp.iloc[-len(date_to_pred):, :]]
            )
    return data
