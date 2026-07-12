import logging

from pydantic import ValidationError
from werkzeug.exceptions import HTTPException

from internal.common import ApiCode, fail_json
from internal.exception import CustomException

logger = logging.getLogger(__name__)


def register_exception_handlers(app):
  """注册全局异常处理器（业务码风格：业务错误 HTTP 200 + code）"""

  @app.errorhandler(CustomException)
  def handle_custom_exception(error):
    """业务异常：按异常自身携带的 code / http_status 返回

    默认 HTTP 200；认证类异常（401/403）保留语义化状态码。
    """
    return fail_json(
      message=error.message,
      data=error.data,
      http_status=error.http_status,
      code=error.code,
    )

  @app.errorhandler(ValidationError)
  def handle_validation_exception(error):
    """参数校验异常：HTTP 200 + code=VALIDATE_ERROR + 字段级错误"""
    return fail_json(
      message="参数校验失败",
      data=error.errors(),
      http_status=200,
      code=ApiCode.VALIDATE_ERROR,
    )

  @app.errorhandler(HTTPException)
  def handle_http_exception(error):
    """协议层异常（路由 404 / 方法 405 / 非法 JSON 400）：保留其 HTTP 状态码"""
    return fail_json(
      message=error.description,
      http_status=error.code or 400,
      code=ApiCode.FAIL,
    )

  @app.errorhandler(Exception)
  def handle_system_exception(error):
    """系统异常：记录完整堆栈，对外返回 500 + 通用提示"""
    logger.exception("未捕获的系统异常: %s", error)
    return fail_json(
      message="服务器内部错误，请稍后重试",
      http_status=500,
      code=ApiCode.SYSTEM_ERROR,
    )
