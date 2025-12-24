import os

# 检查图表文件是否存在
file_path = 'gdp_trend.png'
if os.path.exists(file_path):
    print(f"文件 {file_path} 已成功生成！")
    print(f"文件大小: {os.path.getsize(file_path)} 字节")
else:
    print(f"文件 {file_path} 不存在。")