import pandas as pd

class RegionalService:

    def regional_sales(dataframe: pd.DataFrame):

        regional_data = dataframe.groupby(
            "region"
        )["sales"].sum()

        results = []

        for region, sales in (
            regional_data.items()
        ):

            results.append({

                "region": region,

                "total_sales":
                    round(float(sales), 2)
            })

        return {
            "regional_sales": results
        }


    def regional_forecast(
        dataframe: pd.DataFrame
    ):

        regional_data = dataframe.groupby(
            "region"
        )["sales"].mean()

        forecasts = []

        for region, sales in (
            regional_data.items()
        ):

            forecasts.append({

                "region": region,

                "predicted_demand":
                    round(
                        float(sales * 1.10),
                        2
                    )
            })

        return {
            "regional_forecasts":
                forecasts
        }