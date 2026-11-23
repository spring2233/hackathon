
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# 初始化客户端
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL")
)

# 调用 Qwen 3.7 Plus
response = client.chat.completions.create(
    model="qwen3.7-plus",
    messages=[
        {
            "role": "system",
            "content": "你是一名专业的 AI 教育助手。"
        },
        {
            "role": "user",
            "content": "请根据牛顿第二定律生成一道高中物理选择题，并给出答案和解析。"
        }
    ],
    temperature=0.7,
    max_tokens=2048
)

print(response.choices[0].message.content)

# 查看 Token 使用量
print("\nToken 使用情况：")
print(response.usage)
