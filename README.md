# iOS 备忘录截图封面生成器

> 用 Python 生成以假乱真的 iOS 备忘录截图，专为小红书封面设计

## 特点

- 🔥 **高度仿真**：动态岛、状态栏图标、导航栏、工具栏全部精细还原
- 🎨 **彩色 emoji**：pilmoji 渲染，颜色完全正确
- 📱 **两种风格**：v5（iPhone 14/15 动态岛版）+ v8（带Home键版）
- 📐 **标准尺寸**：1080×1440（3:4，小红书标准）
- ✏️ **内容可定制**：修改几行变量即可生成专属封面

## 快速开始

```bash
# 1. 安装依赖
pip install pillow pilmoji

# 2. 修改内容（编辑脚本顶部的 TITLE 和 lines）

# 3. 生成图片
python scripts/gen_v5.py   # 动态岛版 → output_v5.png
python scripts/gen_v8.py   # Home键版  → output_v8.png
```

## 两种风格对比

| | v5 动态岛版 | v8 Home键版 |
|--|--|--|
| 机型 | iPhone 14/15 | iPhone 13及以前 |
| 特点 | 动态岛 + 绿色电池 | 导航胶囊 + 立体阴影 |
| 适合 | 年轻用户群体 | 大众用户群体 |

## 自定义内容

打开脚本，修改顶部变量：

```python
TITLE = '你的标题'   # ≤12字

lines = [
    ('第一行内容 😊', 'body', 'dark'),
    (None, None, None),          # 空行分段
    ('次要说明文字', 'sm', 'sec'),
    ...
]
```

字体/颜色参数说明见 `references/content-guide.md`

## 依赖

- Python 3.8+
- [Pillow](https://pillow.readthedocs.io/)
- [pilmoji](https://github.com/jay3332/pilmoji)
- Windows 系统字体（微软雅黑）

## License

MIT
