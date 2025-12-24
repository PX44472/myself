#from openai import OpenAI
# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-72e69df0f8e24fc386205d0d5bb82ad6", base_url="https://api.deepseek.com")

def dsllm(prompt):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": prompt}
        ],
        stream=False
    )
    return response.choices[0].message.content