from flask_sqlalchemy import SQLAlchemy
from injector import Binder, Module, Injector
from internal.extension.sql_alchemy import db


class LLMOpsModule(Module):
  def configure(self, binder: Binder):
    """配置依赖注入"""

    # 绑定 SQLAlchemy 实例
    binder.bind(SQLAlchemy, to=db)


# 实例化 Injector
injector = Injector([LLMOpsModule()])