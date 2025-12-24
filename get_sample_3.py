import requests
import json
import time

def fetch_bilibili_food_ranking():
    """
    抓取B站美食区排行榜数据
    """
    url = "https://api.bilibili.com/x/web-interface/ranking/v2?rid=211&type=all"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.bilibili.com/',
        'Accept': 'application/json, text/plain, */*'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data['code'] != 0:
            print(f"API请求失败，错误码：{data['code']}, 错误信息：{data.get('message', '未知错误')}")
            return None
        
        video_list = data['data']['list']
        print(f"成功获取到 {len(video_list)} 条视频数据")
        return video_list
        
    except requests.exceptions.RequestException as e:
        print(f"网络请求失败: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON解析失败: {e}")
        return None
    except KeyError as e:
        print(f"数据格式错误，缺少关键字段: {e}")
        return None

def parse_video_data(video_list):
    """
    解析视频数据
    """
    parsed_data = []
    
    for video in video_list:
        try:
            video_info = {
                'aid': video.get('aid', ''),
                'bvid': video.get('bvid', ''),
                'title': video.get('title', '').replace('\n', ' ').replace(',', '，'),
                '播放量': video.get('stat', {}).get('view', 0),
                '点赞数': video.get('stat', {}).get('like', 0),
                '投币数': video.get('stat', {}).get('coin', 0),
                '属地': video.get('pub_location', '未知'),
                '视频时长(秒)': video.get('duration', 0),
                '视频时长(分:秒)': f"{video.get('duration', 0)//60}:{video.get('duration', 0)%60:02d}",
                'up主': video.get('owner', {}).get('name', ''),
                'up主ID': video.get('owner', {}).get('mid', ''),
                '发布时间': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(video.get('pubdate', 0))) if video.get('pubdate') else '未知',
                '视频分类': video.get('tname', ''),
                '收藏数': video.get('stat', {}).get('favorite', 0),
                '分享数': video.get('stat', {}).get('share', 0),
                '评论数': video.get('stat', {}).get('reply', 0),
                '弹幕数': video.get('stat', {}).get('danmaku', 0)
            }
            parsed_data.append(video_info)
            
        except Exception as e:
            print(f"解析视频数据时出错 (aid: {video.get('aid', '未知')}): {e}")
            continue
    
    return parsed_data

def get_sample_3():
    """
    获取最新的样本3数据
    """
    print("开始抓取B站美食区排行榜数据...")
    print("-" * 50)
    
    video_list = fetch_bilibili_food_ranking()
    if not video_list:
        print("数据抓取失败")
        return None
    
    parsed_data = parse_video_data(video_list)
    if not parsed_data:
        print("数据解析失败")
        return None
    
    # 获取最新的样本3
    if len(parsed_data) >= 3:
        sample_3 = parsed_data[2]  # 第3个元素（索引2）
        return sample_3
    else:
        print("数据不足3条")
        return None

if __name__ == "__main__":
    # 执行函数获取最新样本3
    sample_3 = get_sample_3()
    
    if sample_3:
        print("\n【最新样本3】")
        print(f"视频标题：{sample_3['title']}")
        print(f"BV号：{sample_3['bvid']}")
        print(f"播放量：{sample_3['播放量']:,}")
        print(f"点赞数：{sample_3['点赞数']:,}")
        print(f"投币数：{sample_3['投币数']:,}")
        print(f"属地：{sample_3['属地']}")
        print(f"视频时长：{sample_3['视频时长(分:秒)']}")
        print(f"视频链接：https://www.bilibili.com/video/{sample_3['bvid']}")
        print(f"up主：{sample_3['up主']}")
        print(f"发布时间：{sample_3['发布时间']}")
        print(f"视频分类：{sample_3['视频分类']}")
        print(f"收藏数：{sample_3['收藏数']:,}")
        print(f"分享数：{sample_3['分享数']:,}")
        print(f"评论数：{sample_3['评论数']:,}")
        print(f"弹幕数：{sample_3['弹幕数']:,}")
