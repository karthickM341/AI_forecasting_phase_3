from datetime import datetime
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import (
    seasonal_decompose
)


class SeasonalTrendDetector:

    def detect_trends(
        self,
        dataframe: pd.DataFrame
    ):
        sales_series = dataframe[
            "sales"
        ]
        decomposition = seasonal_decompose(
            sales_series,
            model="additive",
            period=4
        )
        trend_values = (
            decomposition.trend
            .fillna(0)
            .tolist()
        )
        seasonal_values = (
            decomposition.seasonal
            .fillna(0)
            .tolist()
        )
        return {
            "trend_detected": True,
            "trend_values":
                trend_values,
            "seasonal_values":
                seasonal_values,
            "generated_at":
                str(datetime.utcnow())
        }


    def sales_trend_analysis(
        self,
        dataframe: pd.DataFrame
    ):
        average_sales = (
            dataframe["sales"].mean()
        )
        max_sales = (
            dataframe["sales"].max()
        )
        min_sales = (
            dataframe["sales"].min()
        )
        trend = "Stable"
        if max_sales > (
            average_sales * 1.5
        ):

            trend = "High Growth"
        elif min_sales < (
            average_sales * 0.5
        ):

            trend = "Declining"

        return {
            "average_sales":
                round(
                    average_sales,
                    2
                ),
            "max_sales":
                round(
                    max_sales,
                    2
                ),
            "min_sales":
                round(
                    min_sales,
                    2
                ),
            "sales_trend":
                trend
        }

    
    def seasonal_summary(
        self,
        dataframe: pd.DataFrame
    ):
        total_sales = (
            dataframe["sales"].sum()
        )
        average_sales = (
            dataframe["sales"].mean()
        )
        seasonal_strength = round(
            np.std(dataframe["sales"]),
            2
        )
        return {
            "total_sales":
                round(total_sales, 2),
            "average_sales":
                round(average_sales, 2),
            "seasonal_strength":
                seasonal_strength,
            "forecast_status":
                "Seasonal Trend Active"
        }