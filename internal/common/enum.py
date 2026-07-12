from enum import Enum


class ApiCode(int, Enum):
  """业务状态码：0 表示成功，非 0 表示失败"""

  # 成功
  SUCCESS = 0
  # 通用业务失败
  FAIL = 1
  # 资源不存在
  NOT_FOUND = 1001
  # 参数校验失败
  VALIDATE_ERROR = 1002
  # 未认证（登录失效）
  UNAUTHORIZED = 1003
  # 无权限
  FORBIDDEN = 1004
  # 系统内部错误
  SYSTEM_ERROR = 5000
