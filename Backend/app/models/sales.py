from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from datetime import datetime

from app.core.database import Base


class Sales(Base):

    __tablename__ = "sales"

    id = Column(Integer,primary_key=True,index=True)
    product_name = Column(String(100),nullable=False)
    category = Column(String(100),nullable=False)
    region = Column(String(100),nullable=True)
    quantity_sold = Column(Integer,default=0)
    unit_price = Column(Float,default=0.0)
    total_sales = Column(Float,default=0.0)
    sales_date = Column(DateTime,default=datetime.utcnow)
    created_at = Column(DateTime,default=datetime.utcnow)