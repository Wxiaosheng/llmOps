from dotenv import load_dotenv
from os import getenv, path

load_dotenv()

BASE_URL = path.dirname(path.abspath(__name__))
print(f"sqlite:///" + path.join(BASE_URL, getenv("SQLALCHEMY_DATABASE_PATH")))

class Config:
  """应用配置"""

  # SQLAlchemy配置
  SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_URL, getenv("SQLALCHEMY_DATABASE_PATH"))

