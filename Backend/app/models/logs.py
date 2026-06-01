from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Float
)

from datetime import datetime

from app.core.database import Base


class Logs(Base):

    __tablename__ = "logs"

    id = Column(Integer,primary_key=True,index=True)

    username = Column(String(100),nullable=False)

    action = Column(String(100),nullable=False)

    module = Column(String(100),nullable=True)

    status = Column(String(100),default="Success")

    ip_address = Column(String(100),nullable=True)

    response_time = Column(Float,default=0.0)

    created_at = Column(DateTime,default=datetime.utcnow)