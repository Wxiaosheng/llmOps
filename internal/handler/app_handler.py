from dataclasses import dataclass
from uuid import UUID

from flask import request
from injector import inject

from internal.common import success_json
from internal.schema.app_schema import AppReq, AppRes
from internal.service.app_service import AppService


@inject
@dataclass
class AppHandler:
  app_service: AppService

  def create_app(self):
    """创建应用"""
    req = AppReq.model_validate(request.get_json())
    app = self.app_service.create_app(req)
    return success_json(
      message="创建成功",
      data=AppRes.model_validate(app).model_dump(mode="json"),
    )

  def get_app(self, app_id: UUID):
    """查询应用"""
    app = self.app_service.get_app(app_id)
    return success_json(data=AppRes.model_validate(app).model_dump(mode="json"))
