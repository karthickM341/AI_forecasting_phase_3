from datetime import datetime
import pandas as pd
from sklearn.linear_model import (
    LinearRegression
)
from sklearn.metrics import (
    mean_absolute_error,
    r2_score
)


class RetrainingService:

    def __init__(self):
        self.model = LinearRegression()
        self.last_retrained = None


    def train_model(
        self,
        dataframe: pd.DataFrame
    ):

        X = dataframe[[
            "sales"
        ]]

        y = dataframe["demand"]
        self.model.fit(X, y)
        self.last_retrained = (
            datetime.utcnow()
        )

        return {
            "status": "success",
            "message":
                "Model trained successfully",
            "trained_at":
                str(self.last_retrained)
        }

    
    def retrain_model(
        self,
        dataframe: pd.DataFrame
    ):

        X = dataframe[[
            "sales"
        ]]

        y = dataframe["demand"]
        self.model.fit(X, y)
        self.last_retrained = (
            datetime.utcnow()
        )

        return {
            "status": "success",
            "message":
                "AI model retrained successfully",
            "retrained_at":
                str(self.last_retrained)
        }


    def evaluate_model(
        self,
        dataframe: pd.DataFrame
    ):

        X = dataframe[[
            "sales"
        ]]

        y_true = dataframe["demand"]
        predictions = self.model.predict(X)
        mae = mean_absolute_error(
            y_true,
            predictions
        )
        accuracy = r2_score(
            y_true,
            predictions
        )
        return {
            "accuracy":
                round(accuracy * 100, 2),
            "mean_absolute_error":
                round(mae, 2),
            "model_status":
                "Optimized"
        }

    def retraining_status(self):

        return {
            "model": "Linear Regression",
            "last_retrained":
                str(self.last_retrained),
            "auto_retraining":
                "Enabled",
            "status": "Running"
        }