import pandas as pd

class RevenueService:

    def total_revenue(
        dataframe: pd.DataFrame
    ):

        total = dataframe["revenue"].sum()

        return {
            "total_revenue":
                round(float(total), 2)
        }


    def monthly_revenue(
        dataframe: pd.DataFrame
    ):

        monthly = dataframe.groupby(
            "month"
        )["revenue"].sum()

        results = []

        for month, revenue in (
            monthly.items()
        ):

            results.append({
                "month": month,
                "revenue":
                    round(
                        float(revenue),
                        2
                    )
            })

        return {
            "monthly_revenue":
                results
        }

    def revenue_prediction(
        dataframe: pd.DataFrame
    ):

        average_revenue = (
            dataframe["revenue"]
            .mean()
        )
        predicted_revenue = (
            average_revenue * 1.15
        )
        return {

            "predicted_revenue":
                round(
                    float(predicted_revenue),
                    2
                ),
            "status":
                "Predicted"
        }