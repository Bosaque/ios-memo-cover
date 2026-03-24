---
name: ios-memo-cover
description: 生成高仿真 iOS 备忘录截图风格的小红书封面图。支持两种风格：v5（动态岛版，iPhone 14/15风格）和 v8（带Home键版，参照真实截图还原）。当用户需要生成小红书封面、iOS备忘录截图风格图片时使用。
---

# iOS 备忘录截图封面生成器

生成以假乱真的 iOS 备忘录截图，用作小红书封面图。

## 两种风格

| 风格 | 脚本 | 特点 |
|------|------|------|
| **v5** 动态岛版 | `scripts/gen_v5.py` | iPhone 14/15 动态岛 + 彩色emoji + 绿色电池 |
| **v8** Home键版 | `scripts/gen_v8.py` | 参照真实截图 + 导航栏胶囊 + 立体阴影 |

## 使用方法

### 第一步：安装依赖
```bash
pip install pillow pilmoji
```

### 第二步：修改内容

打开脚本，修改顶部 `TITLE` 和 `lines` 列表：

```python
TITLE = '你的标题'   # ≤12字
lines = [
    ('第一行内容', 'body', 'dark'),
    (None, None, None),          # 空行分段
    ('次要文字', 'sm', 'sec'),
    ...
]
```

### 第三步：运行生成
```bash
python scripts/gen_v5.py   # → output_v5.png
python scripts/gen_v8.py   # → output_v8.png
```

## 内容格式

| 字体参数 | 含义 |
|---------|------|
| `'body'` | 正文（33px） |
| `'sm'`   | 小字（29px） |

| 颜色参数 | 含义 |
|---------|------|
| `'dark'` | 黑色 |
| `'sec'`  | 深灰 |
| `'mid'`  | 中灰 |

`None` 行 = 空行分段，约 18-22 行内容填满画面

## 参考

- `references/content-guide.md` — 文案写作指南
- `references/troubleshoot.md` — 常见问题排查
