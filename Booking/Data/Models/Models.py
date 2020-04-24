from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Passenger_model(Base):
    __tablename__="passenger"

    passenger_id=Column(Integer, primary_key=True)
    booking_id=Column(Integer)
    name=Column(String(32))
    age=Column(Integer)
    gender=Column(String(32))
    is_active=Column(Integer)

