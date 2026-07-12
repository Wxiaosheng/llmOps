
from dataclasses import dataclass

from flask import Blueprint, Flask
from injector import inject

from internal.handler import AppHandler, ChatHandler

@inject
@dataclass
class Router:
  app_handler: AppHandler
  chat_handler: ChatHandler

  def register_routes(self, app: Flask):
    """注册路由"""

    api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

    api_bp.add_url_rule('/openai/chat', view_func=self.chat_handler.openai_chat, methods=['POST'])

    api_bp.add_url_rule('/apps', view_func=self.app_handler.create_app, methods=['POST'])
    api_bp.add_url_rule('/apps/<uuid:app_id>', view_func=self.app_handler.get_app, methods=['GET'])

    app.register_blueprint(api_bp)