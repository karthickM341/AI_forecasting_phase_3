from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    Boolean
)

from datetime import datetime

from app.core.database import Base


class Anomaly(Base):

    __tablename__ = "anomalies"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    product_name = Column(
        String,
        nullable=False
    )

    category = Column(
        String,
        nullable=True
    )

    anomaly_score = Column(
        Float,
        default=0.0
    )

    sales_value = Column(Float,default=0.0)

    expected_value = Column(Float,default=0.0)

    anomaly_type = Column(String(100),nullable=True)

    severity = Column(String(100),default="Medium")

    status = Column(String(100),default="Detected")

    is_resolved = Column(Boolean,default=False)

    detected_at = Column(DateTime,default=datetime.utcnow)