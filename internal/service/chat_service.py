
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from flask import current_app
from internal.schema import ChatReq


class ChatService:
  """聊天服务类"""

  def openai_chat(self, req: ChatReq) -> dict:
    """调用 OpenAI 的聊天接口"""
    
    # 1. 构建 prompt（使用 from_template 创建实例）
    prompt = ChatPromptTemplate.from_template("你叫 victree，请你回答用户的提问：{query}")

    # 2. 调用 OpenAI 的聊天接口
    base_url = current_app.config.get('OPENAI_BASE_URL')
    api_key = current_app.config.get('OPENAI_API_KEY')

    llm = ChatOpenAI(
      model_name="glm-5.2",
      base_url=base_url,
      api_key=api_key
    )

    # 3. 输出解析器
    outputParser = StrOutputParser()

    chain = prompt | llm | outputParser
    result = chain.invoke({"query": req.query})

    return {"content": result}
  
  def openai_chat_stream(self, req: ChatReq):
    """流式 openai chat"""
     # 1. 构建 prompt（使用 from_template 创建实例）
    prompt = ChatPromptTemplate.from_template("你叫 victree，请你回答用户的提问：{query}")

    # 2. 调用 OpenAI 的聊天接口
    base_url = current_app.config.get('OPENAI_BASE_URL')
    api_key = current_app.config.get('OPENAI_API_KEY')

    # 为兼容第三方 OpenAI 协议实现，确保 openai 客户端使用正确的 base 和 key
    llm = ChatOpenAI(
      streaming=True,
      model_name="glm-5.2",
      base_url=base_url,
      api_key=api_key
    )

    # 3. 输出解析器
    outputParser = StrOutputParser()

    chain = prompt | llm | outputParser
    
    return chain.stream({ "query": req.query })