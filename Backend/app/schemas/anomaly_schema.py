from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class AnomalySchema(BaseModel):

    product_name: str
    category: str
    region: str
    actual_sales: float = Field(..., ge=0)
    predicted_sales: float = Field(..., ge=0)
    deviation_percentage: float
    anomaly_type: str
    severity_level: str
    detected_at: datetime


class AnomalyResponseSchema(BaseModel):

    success: bool
    message: str
    anomaly: AnomalySchema


class AnomalySummarySchema(BaseModel):

    total_anomalies: int
    critical_anomalies: int
    high_risk_anomalies: int
    medium_risk_anomalies: int
    low_risk_anomalies: int


class AnomalyAlertSchema(BaseModel):

    alert_id: int
    product_name: str
    alert_message: str
    severity_level: str
    status: str
    created_at: datetime


class AnomalyAnalyticsSchema(BaseModel):

    average_deviation: float
    most_affected_region: str
    most_affected_category: str
    anomaly_trend: str
    detection_accuracy: float