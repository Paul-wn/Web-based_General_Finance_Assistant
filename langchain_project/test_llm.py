from typing import List 
from typing_extensions import TypedDict
from langchain_ollama import ChatOllama
import time
def power_calculator(base: int, exponent: int) -> int:
    return base ** exponent

# function_dict = {
#     "power_calculator": power_calculator
# }
# start = time.time()
# prompt = "Hello"
# llm = ChatOllama(model="llama3-groq-tool-use:8b", temperature=0, max_tokens=1000).bind_tools([power_calculator])
# result = llm.invoke(prompt)
# llm2 = ChatOllama(model="llama3.2", temperature=0.7, max_tokens=1000)
# if result.content:
#     print("LLM Completion")
#     print("Time taken:", time.time() - start)
#     # print(result)
#     result = llm2.invoke(prompt)
#     print(result.content)
# else:
#     print("LLM Tool Use")
#     print("Time taken:", time.time() - start)
#     print(result.tool_calls)
#     tool_name = result.tool_calls[0]['name']
#     function_call = function_dict[tool_name](**result.tool_calls[0]['args'])
#     print("Tool call result:", function_call)



llm = ChatOllama(model="hf.co/Float16-cloud/typhoon2-qwen2.5-7b-instruct-gguf:latest", temperature=0, max_tokens=1000).bind_tools([power_calculator])
result = llm.invoke('สวัสดีครับ ช่วยคำนวณ 2 ยกกำลัง 3 ให้หน่อย')
print(result.content)
print(result.tool_calls) 