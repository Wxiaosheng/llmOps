from dataclasses import asdict
from typing import Any

from flask import jsonify

from internal.common import ApiCode
from internal.schema import (
  BaseResponse, SuccessResponse, FailResponse
)


def json(data: BaseResponse, http_status: int = 200):
  """基础响应接口"""
  return jsonify(asdict(data)), http_status


def success_json(message: str | None = None, data: Any = None, http_status: int = 200):
  """响应成功"""
  return json(SuccessResponse(message=message, data=data), http_status)


def fail_json(
  message: str | None = None,
  data: Any = None,
  http_status: int = 200,
  code: ApiCode = ApiCode.FAIL,
):
  """响应失败：默认 HTTP 200，业务结果由 code 区分"""
  return json(FailResponse(code=code, message=message, data=data), http_status)
