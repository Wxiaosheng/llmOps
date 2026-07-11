from sqlalchemy import (
  Column, String, UUID, DateTime
)
from datetime import datetime
from internal.extension.sql_alchemy import db


class App(db.Model):
  """应用"""
  __tablename__ = 'app'

  id: UUID = Column(UUID, primary_key=True)

  name: str = Column(String(255), nullable=False, unique=True)
  icon: str | None = Column(String(255), nullable=True)
  description: str | None = Column(String(255), nullable=True)

  created_at: str = Column(DateTime, nullable=False)
  updated_at: str = Column(DateTime, nullable=False, onupdate=datetime.now)