from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from datetime import datetime

from app.core.database import Base


class Analytics(Base):

    __tablename__ = "analytics"

    id = Column(Integer,primary_key=True,index=True)

    category = Column(String(100),nullable=False)

    total_sales = Column(Float,default=0.0)

    revenue = Column(Float,default=0.0)

    growth_rate = Column(Float,default=0.0)

    forecast_accuracy = Column(Float,default=0.0)

    region = Column(String(100),nullable=True)

    model_used = Column(String(100),nullable=True)

    created_at = Column(DateTime,default=datetime.utcnow)