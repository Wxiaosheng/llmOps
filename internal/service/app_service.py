
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4

from flask_sqlalchemy import SQLAlchemy
from injector import inject

from internal.exception import NotFoundException
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

  def get_app(self, app_id: UUID) -> App:
    app = self.db.session.query(App).get(app_id)

    if not app:
      raise NotFoundException('该应用不存在，请核实后重试')

    return app
