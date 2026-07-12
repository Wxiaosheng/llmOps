from typing import Any

from internal.common import ApiCode


class CustomException(Exception):
  """业务异常基类

  业务异常默认以 HTTP 200 + body 中的 code 表达结果；
  子类通过覆盖 code / http_status 区分业务码与是否需要语义化 HTTP 状态码
  （如认证类异常保留 401/403，便于网关与前端拦截器统一处理）。
  """

  code: ApiCode = ApiCode.FAIL
  message: str = ""
  data: Any = None
  http_status: int = 200

  def __init__(self, message: str | None = None, data: Any = None):
    super().__init__(message)
    self.message = message if message is not None else self.message
    self.data = data if data is not None else self.data


class FAILException(CustomException):
  """通用业务失败"""
  pass


class NotFoundException(CustomException):
  """资源未找到：HTTP 200 + code=NOT_FOUND"""

  code = ApiCode.NOT_FOUND
  http_status = 200


class ValidateException(CustomException):
  """参数校验失败：HTTP 200 + code=VALIDATE_ERROR"""

  code = ApiCode.VALIDATE_ERROR
  http_status = 200


class UnauthorizedException(CustomException):
  """未认证：HTTP 401"""

  code = ApiCode.UNAUTHORIZED
  http_status = 401


class ForbiddenException(CustomException):
  """无权限：HTTP 403"""

  code = ApiCode.FORBIDDEN
  http_status = 403
