from dataclasses import dataclass
from typing import Any

from internal.common import ApiCode


@dataclass
class BaseResponse:
  """基础响应对象"""

  code: ApiCode = ApiCode.SUCCESS
  message: str | None = None
  data: Any = None


@dataclass
class SuccessResponse(BaseResponse):
  """成功响应"""

  code: ApiCode = ApiCode.SUCCESS


@dataclass
class FailResponse(BaseResponse):
  """失败响应"""

  code: ApiCode = ApiCode.FAIL
