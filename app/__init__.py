from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config.config import Config
from config.injector import injector
from internal.exception.handler import register_exception_handlers
from internal.router.router import Router

def create_app():
  app = Flask(__name__)

  # 加载配置
  config = Config()
  app.config.from_object(config)

  # 统一的错误处理
  register_exception_handlers(app=app)

  # 将 Injector 实例注入到 Flask 应用中
  db = injector.get(SQLAlchemy)
  db.init_app(app)
  # 初始化数据库迁移
  Migrate(app, db)

  # 注册路由
  router = injector.get(Router)
  router.register_routes(app)

  return app