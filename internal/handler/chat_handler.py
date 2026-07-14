import json
from dataclasses import dataclass

from flask import Response, current_app, request, stream_with_context
from injector import inject

from internal.common import success_json
from internal.schema import ChatReq, ChatRes
from internal.service import ChatService


@inject
@dataclass
class ChatHandler:
  chat_service: ChatService

  def openai_chat(self):
    """调用 OpenAI 的聊天接口"""
    req = ChatReq.model_validate(request.get_json())
    res = self.chat_service.openai_chat(req)
    return success_json(data=ChatRes.model_validate(res).model_dump())

  def openai_chat_stream(self):
    """流式调用 OpenAI 聊天接口（SSE）"""
    req = ChatReq.model_validate(request.get_json())

    res = self.chat_service.openai_chat_stream(req)  # 惰性生成器，迭代时才真正请求

    @stream_with_context
    def generator():
      try:
        for chunk in res:
          if not chunk:  # 过滤空 chunk，只输出真实内容
            continue
          yield f"data: {json.dumps({'content': chunk}, ensure_ascii=False)}\n\n"
      except Exception as e:
        current_app.logger.exception("openai_chat_stream error: %s", e)
        yield f"data: {json.dumps({'error': str(e)}, ensure_ascii=False)}\n\n"
      finally:
        yield "data: [DONE]\n\n"

    return Response(
      generator(),
      mimetype="text/event-stream",  # 正确的 SSE MIME，不能用 headers 里的野头
      headers={
        "Cache-Control": "no-cache",
        "X-Accel-Buffering": "no",  # 关闭 nginx 缓冲，避免流被攒着不吐
      },
    )

