
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from internal.schema import ChatReq


class ChatService:
  """聊天服务类"""

  def openai_chat(self, req: ChatReq) -> dict:
    """调用 OpenAI 的聊天接口"""
    
    # 1. 构建 prompt
    prompt = ChatPromptTemplate.format_prompt("你叫 victree，请你回答用户的提问：{query}")

    # 2. 调用 OpenAI 的聊天接口
    llm = ChatOpenAI(
      model_name="glm-5.2",
      base_url="https://ark.cn-beijing.volces.com/api/plan/v3",
      api_key="OPENAI_API_KEY"
    )

    # 3. 输出解析器
    outputParser = StrOutputParser()

    chain = prompt | llm | outputParser
    result = chain.invoke({"query": req.query})

    return {"content": result}