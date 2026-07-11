from pydantic import (
  BaseModel,
  Field,
)

class AppReq(BaseModel):
  """创建应用请求参数"""

  name: str = Field(..., max_length=255)
  description: str | None = Field(None,max_length=1000)
  icon: str | None = Field(None, max_length=255)

# model_config 是 Pydantic 2 的配置，表示：
# 在校验/转换一个对象时，Pydantic 可以从对象的属性里读取数据，而不只是从 dict 的键值里读取。
# tips: AppReq 处理的是客户端发来的 json ，这就是 dict，不需要加
class AppRes(BaseModel):
  """创建应用响应参数"""

  model_config = {"from_attributes": True}

  id: str
  name: str
  description: str | None
  icon: str | None
  created_at: str
  updated_at: str