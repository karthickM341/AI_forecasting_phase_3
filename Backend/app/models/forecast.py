from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

from app.core.database import Base


class Forecast(Base):

    __tablename__ = "forecasts"

    id = Column(Integer, primary_key=True, index=True)

    product_name = Column(String(255), nullable=False)

    predicted_sales = Column(Float, nullable=False)

    model_used = Column(String(100), default="LinearRegression")

    accuracy = Column(Float)

    forecast_date = Column(DateTime)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

class ForecastHistory(Base):

    __tablename__ = "forecast_history"

    id = Column(Integer, primary_key=True, index=True)

    product_name = Column(String(255), nullable=False)

    actual_sales = Column(Float)

    predicted_sales = Column(Float)

    model_used = Column(String(255))

    accuracy = Column(Float)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )