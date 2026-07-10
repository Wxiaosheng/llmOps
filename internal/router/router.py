
from dataclasses import dataclass

from flask import Blueprint, Flask
from injector import inject

from internal.handler import AppHandler

url_prefix='/api/v1'

@inject
@dataclass
class Router:
  app_handler: AppHandler

  def register_routes(self, app: Flask):
    """注册路由"""

    api_bp = Blueprint('api/v1', __name__, url_prefix)

    api_bp.add_url_rule('/apps', view_func=self.app_handler.create_app, methods=['POST'])

    app.register_blueprint(api_bp)