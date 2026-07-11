
from dataclasses import dataclass

from flask import jsonify, request
from injector import inject

from internal.schema import ChatReq, ChatRes
from internal.service import ChatService


@inject
@dataclass
class ChatHandler:
  chat_service: ChatService

  def openai_chat(self) -> dict:
    """调用 OpenAI 的聊天接口"""

    req = request.get_json()

    try:
      req = ChatReq.model_validate(req)
    except Exception as e:
      return {"error": str(e)}, 400

    res = self.chat_service.openai_chat(req)

    res = ChatRes.model_validate(res)

    return jsonify(res.model_dump()), 200