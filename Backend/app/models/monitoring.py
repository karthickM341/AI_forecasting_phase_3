from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from datetime import datetime

from app.core.database import Base


class Monitoring(Base):

    __tablename__ = "monitoring"

    id = Column(Integer,primary_key=True,index=True)

    cpu_usage = Column(Float,default=0.0)

    memory_usage = Column(Float,default=0.0)

    disk_usage = Column(Float,default=0.0)

    active_users = Column(Integer,default=0)

    api_response_time = Column(Float,default=0.0)

    server_status = Column(String(100),default="Running")

    created_at = Column(DateTime,default=datetime.utcnow)