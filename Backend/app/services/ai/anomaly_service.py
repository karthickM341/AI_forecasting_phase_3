from datetime import datetime
from sklearn.ensemble import IsolationForest
import pandas as pd


class AnomalyDetectionService:

    def __init__(self):

        self.model = IsolationForest(
            contamination=0.05,
            random_state=42
        )

    def train_model(self, dataframe: pd.DataFrame):

        sales_data = dataframe[[
            "sales"
        ]]
        self.model.fit(sales_data)

        return {
            "status": "success",
            "message":
                "Anomaly model trained successfully"
        }

    def detect_anomalies(
        self,
        dataframe: pd.DataFrame
    ):

        sales_data = dataframe[[
            "sales"
        ]]

        predictions = self.model.fit_predict(
            sales_data
        )

        anomalies = []

        for index, prediction in enumerate(
            predictions
        ):

            if prediction == -1:

                anomalies.append({

                    "row": index,

                    "sales":
                        float(
                            dataframe.iloc[index][
                                "sales"
                            ]
                        ),

                    "status": "Anomaly",

                    "detected_at":
                        str(datetime.utcnow())
                })

        return {

            "total_records":
                len(dataframe),

            "anomalies_detected":
                len(anomalies),

            "anomalies":
                anomalies
        }

    