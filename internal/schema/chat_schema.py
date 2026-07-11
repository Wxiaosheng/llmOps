
from pydantic import BaseModel, Field


class ChatReq(BaseModel):
  """创建聊天请求参数"""

  query: str = Field(..., max_length=1000)


class ChatRes(BaseModel):
  """创建聊天响应参数"""

  model_config = {"from_attributes": True}

  content: str