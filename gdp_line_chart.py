import matplotlib.pyplot as plt
import numpy as np

# 配置matplotlib支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 示例GDP数据（单位：万亿美元）
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
china_gdp = [11.06, 11.23, 12.31, 13.89, 14.34, 14.73, 17.73, 18.10, 18.32]
usa_gdp = [18.21, 18.71, 19.54, 20.61, 21.43, 20.93, 23.32, 25.46, 26.95]
japan_gdp = [4.38, 4.94, 4.88, 4.97, 5.15, 5.05, 4.94, 4.23, 4.23]
germany_gdp = [3.38, 3.47, 3.68, 3.97, 3.86, 3.85, 4.22, 4.07, 4.43]

# 创建折线图
plt.figure(figsize=(10, 6))

# 绘制各国GDP折线
plt.plot(years, china_gdp, label='中国', marker='o', linewidth=2)
plt.plot(years, usa_gdp, label='美国', marker='s', linewidth=2)
plt.plot(years, japan_gdp, label='日本', marker='^', linewidth=2)
plt.plot(years, germany_gdp, label='德国', marker='d', linewidth=2)

# 添加图表标题和坐标轴标签
plt.title('主要国家GDP变化趋势 (2015-2023)', fontsize=16)
plt.xlabel('年份', fontsize=12)
plt.ylabel('GDP (万亿美元)', fontsize=12)

# 添加网格线
plt.grid(True, linestyle='--', alpha=0.7)

# 添加图例
plt.legend(fontsize=10, loc='upper left')

# 设置坐标轴刻度
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 30, 5))

# 调整布局
plt.tight_layout()

# 保存图表
plt.savefig('gdp_trend.png', dpi=300, bbox_inches='tight')
print("图表已保存为 gdp_trend.png")

# 显示图表（如果在交互式环境中运行）
plt.show()