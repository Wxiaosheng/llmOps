
from dataclasses import dataclass

from flask import Response, jsonify, request
from injector import inject

from internal.schema.app_schema import AppReq
from internal.service.app_service import AppService


@inject
@dataclass
class AppHandler:
  app_service: AppService

  def create_app(self) -> Response:
    """创建应用"""

    try:
      req = AppReq.model_validate(request.get_json())
    except Exception as e:
      return {"error": str(e)}, 400
  
    app = self.app_service.create_app(req)

    res = AppReq.model_validate(app)

    return res.model_dump(), 200