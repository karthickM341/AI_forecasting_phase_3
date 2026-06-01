from datetime import datetime
import pandas as pd
import numpy as np


class CategoryAnalyticsService:

    def category_sales_analysis(
        self,
        dataframe: pd.DataFrame
    ):

        category_summary = dataframe.groupby(
            "category"
        )["sales"].sum()

        results = []

        for category, sales in (
            category_summary.items()
        ):

            results.append({

                "category": category,

                "total_sales":
                    round(float(sales), 2)
            })

        return {

            "total_categories":
                len(results),

            "categories":
                results,

            "generated_at":
                str(datetime.utcnow())
        }


    def top_categories(
        self,
        dataframe: pd.DataFrame
    ):

        category_summary = dataframe.groupby(
            "category"
        )["sales"].sum()

        sorted_categories = (
            category_summary
            .sort_values(
                ascending=False
            )
        )

        results = []

        for category, sales in (
            sorted_categories.items()
        ):

            results.append({

                "category": category,

                "sales":
                    round(float(sales), 2)
            })

        return {

            "top_categories":
                results[:5]
        }

    