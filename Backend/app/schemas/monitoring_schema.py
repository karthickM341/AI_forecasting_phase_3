from pydantic import BaseModel
from typing import List
from datetime import datetime


class SystemMetricsSchema(BaseModel):

    cpu_usage: float
    memory_usage: float
    disk_usage: float
    active_users: int
    response_time: float
    server_status: str
    checked_at: datetime


class APIActivitySchema(BaseModel):

    endpoint: str
    method: str
    status_code: int
    response_time: float
    requested_at: datetime


class UserActivitySchema(BaseModel):

    username: str
    activity: str
    module: str
    ip_address: str
    activity_time: datetime


class ForecastMonitoringSchema(BaseModel):

    product_name: str
    forecast_accuracy: float
    prediction_status: str
    generated_at: datetime


class PerformanceAnalyticsSchema(BaseModel):

    total_requests: int
    successful_requests: int
    failed_requests: int
    average_response_time: float
    uptime_percentage: float


class MonitoringDashboardSchema(BaseModel):

    system_metrics: SystemMetricsSchema
    api_activities: List[
        APIActivitySchema
    ]
    user_activities: List[
        UserActivitySchema
    ]
    forecast_monitoring: List[
        ForecastMonitoringSchema
    ]
    performance: PerformanceAnalyticsSchema