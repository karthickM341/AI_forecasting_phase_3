from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class RegionAnalyticsSchema(BaseModel):

    region: str
    total_sales: float = Field(..., ge=0)
    predicted_demand: float = Field(..., ge=0)
    revenue_prediction: float = Field(..., ge=0)
    growth_rate: float


class CategoryAnalyticsSchema(BaseModel):

    category: str
    total_products: int = Field(..., ge=0)
    total_sales: float = Field(..., ge=0)
    demand_forecast: float = Field(..., ge=0)
    top_selling_product: str


class InventoryRiskSchema(BaseModel):

    product_name: str
    current_stock: int = Field(..., ge=0)
    reorder_level: int = Field(..., ge=0)
    risk_level: str
    recommended_action: str


class RevenueAnalyticsSchema(BaseModel):

    total_revenue: float = Field(..., ge=0)
    predicted_revenue: float = Field(..., ge=0)
    profit_margin: float
    monthly_growth: float


class ForecastHistorySchema(BaseModel):

    product_name: str
    actual_sales: float
    predicted_sales: float
    forecast_accuracy: float
    forecast_date: datetime

class AnalyticsDashboardSchema(BaseModel):

    regions: List[RegionAnalyticsSchema]
    categories: List[CategoryAnalyticsSchema]
    inventory_risks: List[InventoryRiskSchema]
    revenue: RevenueAnalyticsSchema
    forecast_history: List[
        ForecastHistorySchema
    ]