from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from pathlib import Path
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text, Numeric
from datetime import datetime, timezone

# DATABASE MODELS
Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'

    RoleID = Column(Integer, primary_key=True, autoincrement=True)
    RoleName = Column(String(100), nullable=False)

    users = relationship('User', back_populates='role_ref') # many users per role

class User(Base):
    __tablename__ = 'users'

    UserID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100), nullable=False)
    Email = Column(String(150), nullable=False, unique=True)
    Mobile = Column(String(20))
    Salt = Column(String(64), nullable=False)
    PasswordHash = Column(String(128), nullable=False)
    CreatedAt = Column(DateTime, default=datetime.now(timezone.utc))

    RoleID = Column(Integer, ForeignKey('roles.RoleID'))

    role = relationship('Role', back_populates='users') # one role per user
    service_requests =  relationship('Service_Request', back_populates='user') # many service requests per user
    audit_logs = relationship('Audit_Log', back_populates='user') # many audit logs per user

class Service_Request(Base):
    __tablename__ = 'service_requests'

    RequestID = Column(Integer, primary_key=True, autoincrement=True)
    ServiceType = Column(String(100), nullable=False)
    Description = Column(Text)
    FeeAmount = Column(Numeric(10, 2), default=0.00)
    Status = Column(String(50), default='Pending')
    CreatedAt = Column(DateTime, default=datetime.now(timezone.utc))

    UserID = Column(Integer, ForeignKey('users.UserID'))

    user = relationship('User', back_populates='service_requests') # one user per service request    

class Audit_Log(Base):
    __tablename__ = 'audit_logs'

    LogID = Column(Integer, primary_key=True, autoincrement=True)
    Action = Column(String(200), nullable=False)
    Timestamp = Column(DateTime, default=datetime.now(timezone.utc))

    UserID = Column(Integer, ForeignKey('users.UserID'))

    user = relationship('User', back_populates='audit_logs') # one user per audit log

# DEPENDENCY INJECTION FUNCTION
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

DB_URL = os.getenv('DB_URL')

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()