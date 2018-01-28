# models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Store(Base):
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    itemname = Column(String(50), unique=True)
    seller = Column(String(80))
    price = Column(Integer)
    itemtype = Column(String(50))

    def __init__(self, itemname=None, seller=None, price=None, itemtype=None ):
        self.itemname = itemname
        self.seller = seller
        self.price = price
        self.itemtype = itemtype

    def __repr__(self):
        return '<Product %r>' % (self.itemname)
