from datetime import datetime
import numpy as np
import pandas as pd
from sklearn.ensemble import (
    RandomForestRegressor
)
from xgboost import XGBRegressor
from sklearn.metrics import (
    mean_absolute_error,
    r2_score
)

class EnsembleForecastService:
    def __init__(self):

        self.random_forest = (
            RandomForestRegressor(
                n_estimators=100,
                random_state=42
            )
        )
        self.xgboost = XGBRegressor(
            n_estimators=100,
            learning_rate=0.1,
            random_state=42
        )

    def train_models(
        self,
        dataframe: pd.DataFrame
    ):

        X = dataframe[[
            "sales"
        ]]

        y = dataframe["demand"]

        self.random_forest.fit(X, y)

        self.xgboost.fit(X, y)

        return {

            "status": "success",

            "message":
                "Ensemble models trained successfully",

            "trained_at":
                str(datetime.utcnow())
        }


    def generate_forecast(
        self,
        dataframe: pd.DataFrame
    ):

        X = dataframe[[
            "sales"
        ]]

        rf_predictions = (
            self.random_forest.predict(X)
        )

        xgb_predictions = (
            self.xgboost.predict(X)
        )

        final_predictions = np.mean(
            [
                rf_predictions,
                xgb_predictions
            ],
            axis=0
        )

        forecasts = []

        for index, prediction in enumerate(
            final_predictions
        ):

            forecasts.append({

                "row": index,

                "predicted_demand":
                    round(
                        float(prediction),
                        2
                    )
            })

        return {

            "total_forecasts":
                len(forecasts),

            "forecasts":
                forecasts,

            "generated_at":
                str(datetime.utcnow())
        }

    def evaluate_models(
        self,
        dataframe: pd.DataFrame
    ):

        X = dataframe[[
            "sales"
        ]]

        y_true = dataframe["demand"]

        rf_predictions = (
            self.random_forest.predict(X)
        )

        xgb_predictions = (
            self.xgboost.predict(X)
        )

        final_predictions = np.mean(
            [
                rf_predictions,
                xgb_predictions
            ],
            axis=0
        )

        mae = mean_absolute_error(
            y_true,
            final_predictions
        )

        accuracy = r2_score(
            y_true,
            final_predictions
        )

        return {

            "mae":
                round(mae, 2),

            "accuracy":
                round(accuracy * 100, 2),

            "status": "Optimized"
        }