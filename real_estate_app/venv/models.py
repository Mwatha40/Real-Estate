from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# User Model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

# Property Model
class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String)
    address = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    property_type = Column(String, nullable=False)  # Apartment, House, etc.
    status = Column(String, default='Available')
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='properties')

User.properties = relationship('Property', order_by=Property.id, back_populates='owner')

# Favorites Table (Many-to-Many Relationship)
favorites = Table(
    'favorites', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('property_id', Integer, ForeignKey('properties.id'))
)
