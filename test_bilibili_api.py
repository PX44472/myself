import requests
import json

# 测试用户提供的美食区API
url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=211&type=all'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.bilibili.com/ranking/all/211/0/3',
}

try:
    response = requests.get(url, headers=headers)
    print(f"状态码: {response.status_code}")
    print(f"响应内容: {response.text[:500]}...")
    
    # 尝试解析JSON
    data = response.json()
    print(f"API返回状态: {data['code']}, 消息: {data['message']}")
    
except Exception as e:
    print(f"错误: {e}")