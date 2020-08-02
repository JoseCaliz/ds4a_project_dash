import joblib as jl


def highlight_current_page(lev_nav, current_page):
    for key in lev_nav.keys():
        if key == current_page:
            lev_nav[key] = True
        else:
            left_nav[key] = False

    return lev_nav


def predict_time_series(data, crime, time_steps):
    models = jl.load('./data/models/time_series_models.pkl')
    prophet_models = ['homicidios', 'hurto_motocicletas', 'hurto_personas']

    if crime in prophet_models:
        # Hacer la prediccion
        return True

    # Hacer la prediccion por xgboost
