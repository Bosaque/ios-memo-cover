# -*- coding: utf-8 -*-
"""
高仿真 iOS 备忘录截图 v5
PIL精准还原，无AI感，像素级控制
跨平台版本：自动识别 Windows / Mac / Linux 字体路径
"""
import os, sys, platform
from PIL import Image, ImageDraw, ImageFont
from pilmoji import Pilmoji

# ══════════════════════════════════════════════
# ✏️ 在这里修改你的内容（每次发帖改这里）
# ══════════════════════════════════════════════
TITLE = '月薪6千在福州存钱记录'   # ≤12字

lines_content = [
    ('之前觉得6千在福州存不了钱 😮', 'body', 'dark'),
    ('房租1200 吃饭800 交通200', 'body', 'dark'),
    ('剩下的不知道哪去了... 😭', 'body', 'dark'),
    (None, None, None),
    ('认真记了3个月账才发现 📒', 'body', 'dark'),
    ('钱都漏在这几个地方 👇', 'body', 'dark'),
    (None, None, None),
    ('🥡 外卖：每月将近600', 'sm', 'sec'),
    ('🧋 奶茶咖啡：400多', 'sm', 'sec'),
    ('🛍️ 周末随便逛逛：300', 'sm', 'sec'),
    (None, None, None),
    ('💡 现在的做法：', 'body', 'dark'),
    ('发工资当天先存2000 💰', 'body', 'dark'),
    ('剩下的才是生活费', 'body', 'dark'),
    ('强制储蓄，不然真存不住', 'body', 'dark'),
    (None, None, None),
    ('自己买菜一周省200左右 🥬', 'sm', 'sec'),
    ('三个月攒了5000多 🎉', 'sm', 'sec'),
    ('对我来说已经很满足了', 'sm', 'sec'),
    (None, None, None),
    ('固定支出没办法省 📌', 'sm', 'sec'),
    ('房租1200 / 话费99 / 健身80', 'sm', 'sec'),
    ('这些认了，省弹性支出就行', 'sm', 'sec'),
    (None, None, None),
    ('不是要抠死自己 🙅', 'body', 'dark'),
    ('找到最大漏钱点堵住就行', 'body', 'dark'),
    (None, None, None),
    ('你们月薪多少，能存多少？', 'sm', 'mid'),
    ('评论区说说 😊', 'sm', 'mid'),
]

OUTPUT = 'output_v5.png'   # 输出文件名（改成你想要的路径）
# ══════════════════════════════════════════════

# ── 自动识别字体路径 ────────────────────────────
def find_font(win_name, mac_name, linux_name):
    system = platform.system()
    if system == 'Windows':
        path = f'C:/Windows/Fonts/{win_name}'
    elif system == 'Darwin':  # Mac
        candidates = [
            f'/System/Library/Fonts/{mac_name}',
            f'/Library/Fonts/{mac_name}',
            os.path.expanduser(f'~/Library/Fonts/{mac_name}'),
        ]
        path = next((p for p in candidates if os.path.exists(p)), candidates[0])
    else:  # Linux
        candidates = [
            f'/usr/share/fonts/truetype/wqy/{linux_name}',
            f'/usr/share/fonts/opentype/noto/{linux_name}',
            f'/usr/share/fonts/{linux_name}',
        ]
        path = next((p for p in candidates if os.path.exists(p)), candidates[0])
    if not os.path.exists(path):
        print(f'⚠️  字体未找到: {path}，使用系统默认字体')
        return None
    return path

FONT_REG  = find_font('msyh.ttc',   'PingFang.ttc',  'wqy-microhei.ttc')
FONT_BOLD = find_font('msyhbd.ttc', 'PingFang.ttc',  'wqy-microhei.ttc')
FONT_SYM  = find_font('seguisym.ttf','Arial Unicode MS.ttf','DejaVuSans.ttf')

def load_font(path, size):
    if path and os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

# ── 颜色 ─────────────────────────────────────
bg        = (255, 255, 255)
black     = (0, 0, 0)
dark      = (0, 0, 0)
gray_sec  = (60, 60, 67)
gray_mid  = (142, 142, 147)
gray_lt   = (199, 199, 204)
divider   = (209, 209, 214)
ios_blue  = (0, 122, 255)
ios_green = (52, 199, 89)
cursor_c  = (0, 122, 255)
dyn_black = (0, 0, 0)
toolbar_bg= (249, 249, 249)

# ── 字体 ─────────────────────────────────────
f_time    = load_font(FONT_REG,  26)
f_nav     = load_font(FONT_REG,  30)
f_title   = load_font(FONT_BOLD, 36)
f_body    = load_font(FONT_REG,  33)
f_body_sm = load_font(FONT_REG,  29)
f_small   = load_font(FONT_REG,  23)
f_chevron = load_font(FONT_BOLD, 42)
f_icon_sym= load_font(FONT_SYM,  30)

# ── 颜色映射 ──────────────────────────────────
color_map = {'dark': dark, 'sec': gray_sec, 'mid': gray_mid, 'lt': gray_lt}
font_map  = {'body': f_body, 'sm': f_body_sm}

# ── 画布 ─────────────────────────────────────
W, H = 1080, 1440
img = Image.new('RGB', (W, H), bg)
d   = ImageDraw.Draw(img)

# ── 工具函数 ─────────────────────────────────
def draw_signal(x, y, color):
    bar_w, gap = 6, 4
    heights = [10, 16, 22, 29]
    base = y + 30
    for i, h in enumerate(heights):
        bx = x + i * (bar_w + gap)
        d.rounded_rectangle([(bx, base-h),(bx+bar_w, base)], radius=2, fill=color)

def draw_wifi(x, y, color):
    cx, cy = x+17, y+30
    d.ellipse([(cx-4,cy-4),(cx+4,cy+4)], fill=color)
    for r, lw in [(9,4),(16,4),(23,4)]:
        d.arc([cx-r,cy-r,cx+r,cy+r], start=215, end=325, fill=color, width=lw)

def draw_battery(x, y, pct=74):
    bw, bh, rx = 50, 24, 5
    d.rounded_rectangle([(x,y),(x+bw,y+bh)], radius=rx, outline=black, width=2)
    hx, hy = x+bw+2, y+(bh-12)//2
    d.rounded_rectangle([(hx,hy),(hx+5,hy+12)], radius=2, fill=black)
    iw = int((bw-6)*pct/100)
    if iw > 0:
        d.rounded_rectangle([(x+3,y+3),(x+3+iw,y+bh-3)], radius=3, fill=ios_green)

# ══════════════════════════════════════════════
# 1. 动态岛
# ══════════════════════════════════════════════
status_h = 58
d.rectangle([(0,0),(W,status_h)], fill=bg)

di_w, di_h = 252, 36
di_x = (W - di_w) // 2
di_y = 12
d.rounded_rectangle([(di_x,di_y),(di_x+di_w,di_y+di_h)], radius=18, fill=dyn_black)
cam_cx = di_x + di_w - 22
cam_cy = di_y + di_h // 2
d.ellipse([(cam_cx-8,cam_cy-8),(cam_cx+8,cam_cy+8)], fill=(20,20,20))
d.ellipse([(cam_cx-4,cam_cy-4),(cam_cx+4,cam_cy+4)], fill=(35,35,35))
sen_cx = cam_cx - 24
d.ellipse([(sen_cx-4,cam_cy-4),(sen_cx+4,cam_cy+4)], fill=(25,25,25))

d.text((44, 17), '22:17', font=f_time, fill=black)
batt_x = W - 116
draw_battery(batt_x, 18, pct=74)
draw_wifi(batt_x-56, 14, color=black)
draw_signal(batt_x-112, 14, color=black)

y = status_h

# ══════════════════════════════════════════════
# 2. 导航栏
# ══════════════════════════════════════════════
nav_h = 78
d.rectangle([(0,y),(W,y+nav_h)], fill=bg)
d.text((32, y+18), '‹', font=f_chevron, fill=ios_blue)
d.text((64, y+23), '备忘录', font=f_nav, fill=ios_blue)
d.text((W-84, y+23), '完成', font=f_nav, fill=ios_blue)
d.line([(0,y+nav_h-1),(W,y+nav_h-1)], fill=divider, width=1)
y += nav_h

# ══════════════════════════════════════════════
# 3. 内容区
# ══════════════════════════════════════════════
px     = 56
LINE_H = 52
PARA_H = 20
y += 36

d.text((px, y), TITLE, font=f_title, fill=dark)
y += 62

lines = [(t, font_map.get(f, f_body), color_map.get(c, dark))
         for t, f, c in lines_content]

with Pilmoji(img) as p:
    for text, font, color in lines:
        if text is None:
            y += PARA_H
            continue
        p.text((px, y), text, font=font, fill=color)
        y += LINE_H

# ══════════════════════════════════════════════
# 4. 底部工具栏
# ══════════════════════════════════════════════
tool_y = H - 108
d.rectangle([(0,tool_y),(W,H)], fill=toolbar_bg)
d.line([(0,tool_y),(W,tool_y)], fill=divider, width=1)

tool_icons = [('⊞','表格'),('☑','勾选'),('⬜','图片'),('⊙','相机'),('✎','画笔'),('⊡','扫描')]
step = (W - 80) // len(tool_icons)
ix = 40
for sym, label in tool_icons:
    try:
        tw2 = d.textbbox((0,0), sym, font=f_icon_sym)
        d.text((ix-(tw2[2]-tw2[0])//2, tool_y+18), sym, font=f_icon_sym, fill=gray_mid)
    except:
        tw2 = d.textbbox((0,0), label, font=f_small)
        d.text((ix-(tw2[2]-tw2[0])//2, tool_y+20), label, font=f_small, fill=gray_mid)
    ix += step

home_w = 260
hx = (W - home_w) // 2
d.rounded_rectangle([(hx, H-16),(hx+home_w, H-8)], radius=4, fill=(180,180,182))

img.save(OUTPUT)
print(f'[OK] {OUTPUT}')
