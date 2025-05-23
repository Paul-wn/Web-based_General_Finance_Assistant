from typing import List , Union , Optional
from typing_extensions import TypedDict
from langchain_ollama import ChatOllama
import time
import asyncio

# def power_calculator(base: int, exponent: int) -> int:
#     return base ** exponent



# llm = ChatOllama(model="hf.co/Float16-cloud/typhoon2-qwen2.5-7b-instruct-gguf:latest", temperature=0, max_tokens=1000).bind_tools([power_calculator])
# result = llm.invoke('สวัสดีครับ ช่วยคำนวณ 2 ยกกำลัง 3 ให้หน่อย')
# print(result.content)
# print(result.tool_calls) 

class Ollama():
    def __init__(self, model:str = 'hf.co/Float16-cloud/typhoon2-qwen2.5-7b-instruct-gguf:latest', tool_calls: Optional[List] = []):
        self.tool_calls = tool_calls
        self.model = model

    def generate(self, prompt: str, temperature: float = 0.0, max_tokens: int = 1000) -> str:
        llm = ChatOllama(model=self.model, temperature=temperature, max_tokens=max_tokens).bind_tools(self.tool_calls)
        result =  llm.invoke(prompt)
        return f"{result.content , result.tool_calls}"

