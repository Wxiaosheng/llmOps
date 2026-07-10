
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

from flask_sqlalchemy import SQLAlchemy
from injector import inject

from internal.model import App
from internal.schema import AppReq

@inject
@dataclass
class AppService:

  db: SQLAlchemy

  def create_app(self, req: AppReq):
    """创建应用"""
    app = App(
      id=uuid4(),
      name=req.name,
      description=req.description,
      icon=req.icon,
      created_at=datetime.now(),
      updated_at=datetime.now()
    )
    self.db.session.add(app)
    self.db.session.commit()
    return app


