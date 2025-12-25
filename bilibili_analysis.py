import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('bilibili_food_ranking.csv')

fig = plt.figure(figsize=(16, 7))

plt.subplot(1, 2, 1)
province_counts = df['属地'].value_counts().sort_values(ascending=False)
colors = plt.cm.Set3(range(len(province_counts)))
bars = plt.bar(province_counts.index, province_counts.values, color=colors)
plt.title('B站美食赛道UP主省份分布', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('省份/地区', fontsize=12)
plt.ylabel('UP主数量', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3, linestyle='--')

for i, (bar, value) in enumerate(zip(bars, province_counts.values)):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
             str(value), ha='center', va='bottom', fontsize=9)

plt.subplot(1, 2, 2)
scatter = plt.scatter(df['播放量'], df['点赞数'], 
                      c=df['点赞数']/df['播放量'], 
                      cmap='YlOrRd', 
                      alpha=0.6, 
                      s=50,
                      edgecolors='black', 
                      linewidth=0.5)

plt.title('播放量与点赞数关系散点图', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('播放量', fontsize=12)
plt.ylabel('点赞数', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')

cbar = plt.colorbar(scatter)
cbar.set_label('点赞率（点赞数/播放量）', fontsize=10)

plt.xscale('log')
plt.yscale('log')

plt.tight_layout()
plt.savefig('bilibili_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("图表已生成并保存为 'bilibili_analysis.png'")
print("\n=== 数据统计摘要 ===")
print(f"总视频数: {len(df)}")
print(f"总播放量: {df['播放量'].sum():,}")
print(f"平均播放量: {df['播放量'].mean():,.0f}")
print(f"最高播放量: {df['播放量'].max():,}")
print(f"平均点赞数: {df['点赞数'].mean():,.0f}")
print(f"最高点赞数: {df['点赞数'].max():,}")

print("\n=== 省份分布Top 10 ===")
print(province_counts.head(10))

print("\n=== 播放量Top 5视频 ===")
top_videos = df.nlargest(5, '播放量')[['title', '播放量', '点赞数', '属地', 'up主', 'bvid']]
for idx, row in top_videos.iterrows():
    print(f"\n播放量: {row['播放量']:,} | 点赞数: {row['点赞数']:,}")
    print(f"标题: {row['title']}")
    print(f"UP主: {row['up主']} ({row['属地']})")
    print(f"链接: https://www.bilibili.com/video/{row['bvid']}")

print("\n=== 点赞率Top 5视频 ===")
df['点赞率'] = df['点赞数'] / df['播放量']
top_like_rate = df.nlargest(5, '点赞率')[['title', '播放量', '点赞数', '点赞率', '属地', 'up主', 'bvid']]
for idx, row in top_like_rate.iterrows():
    print(f"\n点赞率: {row['点赞率']:.4f} ({row['点赞率']*100:.2f}%)")
    print(f"播放量: {row['播放量']:,} | 点赞数: {row['点赞数']:,}")
    print(f"标题: {row['title']}")
    print(f"UP主: {row['up主']} ({row['属地']})")
    print(f"链接: https://www.bilibili.com/video/{row['bvid']}")
