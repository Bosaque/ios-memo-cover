# 常见问题排查

## 安装问题

### pilmoji 安装失败
```bash
pip install pilmoji --upgrade
# 如果还失败：
pip install pilmoji --no-deps
pip install requests
```

### emoji 显示为方框
原因：系统缺少 emoji 字体
解决：确保已安装 pilmoji，脚本用 `Pilmoji(img)` 渲染

## 字体问题

### 中文显示乱码
原因：字体路径错误
解决：检查字体路径，Windows 默认：
- `C:/Windows/Fonts/msyh.ttc`（微软雅黑）
- `C:/Windows/Fonts/msyhbd.ttc`（微软雅黑粗体）
- `C:/Windows/Fonts/seguisym.ttf`（Segoe UI Symbol）

Mac/Linux 需修改字体路径：
```python
# Mac
f_body = ImageFont.truetype('/System/Library/Fonts/PingFang.ttc', 33)
# Linux
f_body = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 33)
```

## 图片问题

### 内容空白太多
原因：lines 行数不够
解决：增加内容到约 18-22 行非None行

### 内容被截断
原因：行数太多超出画面
解决：减少内容，或把 `LINE_H` 从 52 改为 48

## 输出路径
默认输出到脚本运行目录：
- v5 → `output_v5.png`
- v8 → `output_v8.png`
