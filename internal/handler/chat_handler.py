from dataclasses import dataclass

from flask import request
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
