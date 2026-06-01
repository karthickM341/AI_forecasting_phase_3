from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class ForecastCreateSchema(BaseModel):

    product_name: str
    category: str
    region: str
    historical_sales: float = Field(..., ge=0)
    inventory_stock: int = Field(..., ge=0)


class ForecastResponseSchema(BaseModel):

    forecast_id: int
    product_name: str
    category: str
    region: str
    predicted_demand: float
    predicted_revenue: float
    forecast_accuracy: float
    trend: str
    risk_level: str
    generated_at: datetime


class RealTimeForecastSchema(BaseModel):

    live_sales: float
    current_demand: float
    forecast_status: str
    active_users: int
    last_updated: datetime


class ForecastHistorySchema(BaseModel):

    product_name: str
    actual_sales: float
    predicted_sales: float
    accuracy: float
    created_at: datetime

class ForecastAnalyticsSchema(BaseModel):

    total_forecasts: int
    average_accuracy: float
    high_risk_products: int
    low_stock_products: int
    overall_trend: str

class ForecastDashboardSchema(BaseModel):

    realtime: RealTimeForecastSchema
    analytics: ForecastAnalyticsSchema
    history: List[ForecastHistorySchema]