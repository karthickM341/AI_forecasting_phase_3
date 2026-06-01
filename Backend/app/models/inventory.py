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


class Inventory(Base):

    __tablename__ = "inventory"

    id = Column(Integer,primary_key=True,index=True)

    product_name = Column(String(100),nullable=False)

    category = Column(String(100),nullable=False)

    sku = Column(String,unique=True,nullable=False)

    stock_quantity = Column(Integer,default=0)

    reorder_level = Column(Integer,default=10)

    unit_price = Column(Float,default=0.0)

    supplier = Column(String(100),nullable=True)

    warehouse_location = Column(String(100),nullable=True)

    stock_status = Column(String(100),default="Available")

    is_active = Column(Boolean,default=True)

    created_at = Column(DateTime,default=datetime.utcnow)

    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)