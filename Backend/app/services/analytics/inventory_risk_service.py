from datetime import datetime
import pandas as pd

class InventoryRiskService:

    def analyze_inventory_risk(
        self,
        dataframe: pd.DataFrame
    ):
        results = []
        for _, row in dataframe.iterrows():

            stock = row["stock"]
            reorder_level = row[
                "reorder_level"
            ]

            risk_level = "Low"
            if stock <= 0:
                risk_level = "Critical"
            elif stock <= reorder_level:
                risk_level = "High"
            elif stock <= (
                reorder_level * 1.5
            ):
                risk_level = "Medium"
            results.append({
                "product_name":
                    row["product_name"],
                "category":
                    row["category"],
                "current_stock":
                    int(stock),
                "reorder_level":
                    int(reorder_level),
                "risk_level":
                    risk_level
            })

        return {

            "total_products":
                len(results),
            "inventory_risks":
                results,
            "generated_at":
                str(datetime.utcnow())
        }

    