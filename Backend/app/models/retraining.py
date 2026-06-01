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


class Retraining(Base):

    __tablename__ = "retraining"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    model_name = Column(
        String,
        nullable=False
    )

    previous_accuracy = Column(
        Float,
        default=0.0
    )

    updated_accuracy = Column(
        Float,
        default=0.0
    )

    training_dataset = Column(
        String,
        nullable=True
    )

    training_status = Column(String(100),default="Completed")

    retraining_trigger = Column(String(100),nullable=True)

    execution_time = Column(Float,default=0.0)

    is_active = Column(Boolean,default=True)

    created_at = Column(DateTime,default=datetime.utcnow)