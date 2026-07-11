from pydantic import (
  BaseModel,
  Field,
)

class AppReq(BaseModel):
  """创建应用请求参数"""
  model_config = {"from_attributes": True}

  name: str = Field(..., max_length=255)
  description: str | None = Field(None,max_length=1000)
  icon: str | None = Field(None, max_length=255)

class AppRes(BaseModel):
  """创建应用响应参数"""

  model_config = {"from_attributes": True}

  id: str
  name: str
  description: str | None
  icon: str | None
  created_at: str
  updated_at: str