from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


W = 1242
H = 1660
BG = "#F6F1E8"
INK = "#1F1F1B"
MUTED = "#6D685F"
ACCENT = "#C5533D"
TEAL = "#5A8E8A"
TEAL_SOFT = "#DCEBEB"
LINE = "#D8D0C6"
CARD = "#FDFBF7"

ROOT = Path("/Users/cecilialiu/Documents/Codex/ai-content")
OUT = ROOT / "output" / "xhs-api-pack"
FONT_REG = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FONT_BOLD = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_LIGHT = "/System/Library/Fonts/STHeiti Light.ttc"
SRC_CLAUDE = OUT / "src-claude-code-hero.png"
SRC_OPENCLAW = OUT / "src-openclaw-hero.png"
SRC_IMMERSIVE = OUT / "src-immersive-translate-hero.png"
SRC_APIKEY = OUT / "src-google-ai-studio-apikey.png"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def draw_multiline(draw: ImageDraw.ImageDraw, x: int, y: int, lines, fnt, fill=INK, gap=10):
    current_y = y
    for line in lines:
        draw.text((x, current_y), line, font=fnt, fill=fill)
        bbox = draw.textbbox((x, current_y), line, font=fnt)
        current_y = bbox[3] + gap
    return current_y


def draw_title(draw, text, x, y, size=102, color=INK):
    return draw_multiline(draw, x, y, text.split("\n"), font(FONT_BOLD, size), fill=color, gap=8)


def draw_body(draw, lines, x, y, size=54, color=INK, gap=18):
    return draw_multiline(draw, x, y, lines, font(FONT_LIGHT, size), fill=color, gap=gap)


def rounded(draw, xy, radius=36, fill=CARD, outline=None, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def line(draw, pts, width=12, fill=TEAL):
    draw.line(pts, fill=fill, width=width, joint="curve")


def device_card(draw, x, y, w, h, title, subtitle=None, bars=4):
    rounded(draw, (x, y, x + w, y + h), radius=32, fill=CARD, outline=LINE, width=3)
    draw.text((x + 28, y + 22), title, font=font(FONT_BOLD, 34), fill=INK)
    if subtitle:
        draw.text((x + 28, y + 70), subtitle, font=font(FONT_LIGHT, 24), fill=MUTED)
    bx = x + 28
    by = y + 118
    for i in range(bars):
        bw = int((w - 56) * (0.72 + 0.2 * ((i % 2) == 0)))
        bh = 16 if i < bars - 1 else 24
        rounded(draw, (bx, by + i * 34, bx + bw, by + i * 34 + bh), radius=8, fill=TEAL_SOFT)
    rounded(draw, (x + w - 96, y + 24, x + w - 32, y + 88), radius=16, fill="#FFF2EE", outline=None)
    draw.line((x + w - 70, y + 38, x + w - 46, y + 38), fill=ACCENT, width=5)
    draw.line((x + w - 70, y + 54, x + w - 40, y + 54), fill=ACCENT, width=5)
    draw.line((x + w - 70, y + 70, x + w - 50, y + 70), fill=ACCENT, width=5)


def tag(draw, x, y, text, fill=TEAL_SOFT, fg=INK):
    f = font(FONT_BOLD, 30)
    bbox = draw.textbbox((0, 0), text, font=f)
    w = bbox[2] - bbox[0] + 46
    h = bbox[3] - bbox[1] + 26
    rounded(draw, (x, y, x + w, y + h), radius=24, fill=fill)
    draw.text((x + 23, y + 12), text, font=f, fill=fg)
    return w


def cover_crop(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    target_w, target_h = size
    src_w, src_h = img.size
    scale = max(target_w / src_w, target_h / src_h)
    resized = img.resize((int(src_w * scale), int(src_h * scale)))
    left = max(0, (resized.width - target_w) // 2)
    top = max(0, (resized.height - target_h) // 2)
    return resized.crop((left, top, left + target_w, top + target_h))


def paste_image_card(base: Image.Image, x: int, y: int, w: int, h: int, path: Path, radius: int = 28):
    if not path.exists():
        return
    img = Image.open(path).convert("RGB")
    img = cover_crop(img, (w, h))
    mask = Image.new("L", (w, h), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle((0, 0, w, h), radius=radius, fill=255)
    base.paste(img, (x, y), mask)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle((x, y, x + w, y + h), radius=radius, outline=LINE, width=3)


def pipe_network(draw):
    line(draw, (622, 430, 622, 910), width=34)
    line(draw, (622, 560, 360, 560), width=26)
    line(draw, (622, 620, 890, 620), width=26)
    line(draw, (622, 780, 622, 1150), width=26)
    for cx, cy in [(622, 560), (622, 620), (622, 780)]:
        draw.ellipse((cx - 24, cy - 24, cx + 24, cy + 24), fill=ACCENT)


def page_base():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw.line((92, 84, W - 92, 84), fill=LINE, width=3)
    return img, draw


def page_1():
    img, draw = page_base()
    draw_title(draw, "普通人为什么\n也要懂 API", 102, 138, size=104)
    draw.text((106, 398), "一根水管", font=font(FONT_BOLD, 58), fill=ACCENT)
    draw.text((106, 468), "接活 3 个 AI 工具", font=font(FONT_LIGHT, 52), fill=INK)
    pipe_network(draw)
    device_card(draw, 132, 686, 280, 248, "Claude Code", "coding")
    device_card(draw, 818, 744, 292, 248, "OpenClaw", "agent")
    device_card(draw, 470, 1118, 302, 248, "翻译插件", "browser")
    x = 116
    for txt in ["Claude Code", "OpenClaw", "翻译插件"]:
        tw = tag(draw, x, 1450, txt, fill="#ECE6DD")
        x += tw + 18
    return img


def page_2():
    img, draw = page_base()
    lines = ["很多人不是不会用 AI", "", "而是不会接自己的 API", "", "所以只能一直用", "别人套好壳的版本", "", "功能更少", "价格还更贵"]
    y = 170
    for line_text in lines:
        size = 78 if "不会接自己的 API" in line_text else 62
        color = ACCENT if "不会接自己的 API" in line_text else INK
        if line_text == "":
            y += 34
            continue
        y = draw_multiline(draw, 110, y, [line_text], font(FONT_BOLD if size > 70 else FONT_LIGHT, size), fill=color, gap=10)
    draw.text((110, 1440), "这就是很多人卡住的地方", font=font(FONT_LIGHT, 34), fill=MUTED)
    return img


def page_3():
    img, draw = page_base()
    draw.text((112, 132), "AI 公司 = 自来水厂", font=font(FONT_BOLD, 48), fill=INK)
    draw.text((112, 194), "API = 你家的水管", font=font(FONT_BOLD, 48), fill=ACCENT)
    draw.text((112, 256), "工具 = 洗衣机 / 花洒 / 洗碗机", font=font(FONT_BOLD, 48), fill=INK)
    rounded(draw, (462, 364, 782, 520), radius=36, fill="#FFF7F0", outline=LINE, width=3)
    draw.text((530, 410), "AI 水厂", font=font(FONT_BOLD, 54), fill=INK)
    pipe_network(draw)
    device_card(draw, 110, 666, 286, 260, "编程工具", "Claude Code")
    device_card(draw, 844, 690, 288, 260, "AI 助手", "OpenClaw")
    device_card(draw, 476, 1118, 292, 260, "翻译插件", "Immersive")
    draw.text((112, 1440), "你买的不是某个工具", font=font(FONT_BOLD, 58), fill=INK)
    draw.text((112, 1512), "而是“水”，接到哪里，由你决定", font=font(FONT_LIGHT, 52), fill=ACCENT)
    return img


def page_4():
    img, draw = page_base()
    draw.text((112, 162), "懂 API", font=font(FONT_BOLD, 90), fill=INK)
    draw.text((112, 272), "不是让你变程序员", font=font(FONT_LIGHT, 60), fill=MUTED)
    draw.text((112, 392), "而是让你可以：", font=font(FONT_BOLD, 62), fill=ACCENT)
    items = [("更省钱", "少为套壳和冗余订阅付费"), ("接更多工具", "同一份模型能力接不同产品"), ("不被单个平台绑死", "工具换了，底层能力还在")]
    y = 560
    for title, desc in items:
        rounded(draw, (112, y, 1130, y + 220), radius=34, fill=CARD, outline=LINE, width=3)
        draw.ellipse((148, y + 60, 220, y + 132), fill=TEAL)
        draw.text((258, y + 44), title, font=font(FONT_BOLD, 52), fill=INK)
        draw.text((258, y + 120), desc, font=font(FONT_LIGHT, 34), fill=MUTED)
        y += 256
    return img


def mock_code_panel(draw, x, y, w, h):
    rounded(draw, (x, y, x + w, y + h), radius=28, fill="#102129")
    rounded(draw, (x + 24, y + 24, x + 120, y + 54), radius=12, fill="#1D3A45")
    draw.text((x + 40, y + 27), "Provider", font=font(FONT_LIGHT, 20), fill="#D6E9E7")
    draw.text((x + 24, y + 82), "anthropic >", font=font(FONT_BOLD, 28), fill="#D4F0EE")
    for i, l in enumerate([0.82, 0.68, 0.75, 0.54, 0.79, 0.42]):
        rounded(draw, (x + 24, y + 146 + i * 52, x + 24 + int((w - 48) * l), y + 168 + i * 52), radius=8, fill="#C6DDD9")


def page_5():
    img, draw = page_base()
    draw.text((106, 146), "案例 1：Claude Code", font=font(FONT_BOLD, 62), fill=INK)
    body = ["接自己的 API 后", "后台跑什么模型", "你自己决定", "", "不一定非得买原生订阅", "成本会更可控"]
    draw_body(draw, body, 106, 310, size=54, gap=20)
    paste_image_card(img, 628, 250, 496, 1024, SRC_CLAUDE)
    draw.text((648, 1316), "同样是 coding，底层模型你自己选", font=font(FONT_LIGHT, 28), fill=MUTED)
    return img


def mock_open_source_panel(draw, x, y, w, h):
    rounded(draw, (x, y, x + w, y + h), radius=28, fill=CARD, outline=LINE, width=3)
    rounded(draw, (x + 28, y + 28, x + w - 28, y + 104), radius=18, fill="#111E23")
    draw.text((x + 52, y + 44), "OpenClaw", font=font(FONT_BOLD, 34), fill="#F2F7F6")
    draw.text((x + 52, y + 84), "repo / config / provider", font=font(FONT_LIGHT, 22), fill="#D2E6E1")
    for col in range(2):
        for row in range(2):
            xx = x + 34 + col * (w // 2 - 10)
            yy = y + 156 + row * 238
            rounded(draw, (xx, yy, xx + w // 2 - 56, yy + 190), radius=22, fill="#F2F8F7")
            draw.text((xx + 22, yy + 20), "配置模块", font=font(FONT_BOLD, 28), fill=INK)
            for i in range(3):
                rounded(draw, (xx + 22, yy + 70 + i * 34, xx + 180 + 70 * i, yy + 86 + i * 34), radius=8, fill=TEAL_SOFT)


def page_6():
    img, draw = page_base()
    draw.text((108, 138), "案例 2：OpenClaw", font=font(FONT_BOLD, 62), fill=INK)
    draw_body(draw, ["很多开源工具", "本身不送模型", "", "你要自己把 API 接进去", "它才真正活过来"], 108, 256, size=54, gap=20)
    paste_image_card(img, 358, 650, 762, 760, SRC_OPENCLAW)
    draw.text((108, 1460), "不会 API，就只能看别人用", font=font(FONT_BOLD, 64), fill=ACCENT)
    return img


def mock_translation_panel(draw, x, y, w, h):
    rounded(draw, (x, y, x + w, y + h), radius=28, fill=CARD, outline=LINE, width=3)
    rounded(draw, (x + 22, y + 22, x + w - 22, y + 86), radius=18, fill="#EEF5F4")
    draw.text((x + 40, y + 39), "沉浸式翻译", font=font(FONT_BOLD, 32), fill=INK)
    rounded(draw, (x + 30, y + 132, x + w // 2 - 12, y + h - 34), radius=22, fill="#FFF8F1")
    rounded(draw, (x + w // 2 + 12, y + 132, x + w - 30, y + h - 34), radius=22, fill="#F0F6F8")
    for col_x in [x + 48, x + w // 2 + 30]:
        for i in range(7):
            bw = 160 + (i % 3) * 42
            rounded(draw, (col_x, y + 168 + i * 54, col_x + bw, y + 184 + i * 54), radius=8, fill="#D9E8E7")


def page_7():
    img, draw = page_base()
    draw.text((106, 144), "案例 3：沉浸式翻译", font=font(FONT_BOLD, 58), fill=INK)
    lines = ["免费版能用", "但质量一般", "", "接上自己的 API Key 后", "调用的是你选的大模型", "翻译质量会明显更好"]
    y = 310
    for line_text in lines:
        if line_text == "":
            y += 26
            continue
        col = ACCENT if "API Key" in line_text or "大模型" in line_text else INK
        y = draw_multiline(draw, 106, y, [line_text], font(FONT_BOLD if col == ACCENT else FONT_LIGHT, 52), fill=col, gap=18)
    paste_image_card(img, 624, 248, 500, 1120, SRC_IMMERSIVE)
    return img


def page_8():
    img, draw = page_base()
    draw_title(draw, "一根水管\n接了三台电器", 316, 188, size=90)
    x = 196
    for txt in ["编程工具", "AI 助手", "翻译插件"]:
        tw = tag(draw, x, 724, txt, fill=TEAL_SOFT)
        x += tw + 26
    draw_title(draw, "这就是 API", 398, 980, size=96, color=ACCENT)
    draw_body(draw, ["最值得普通人理解的地方"], 308, 1106, size=52, color=INK)
    return img


def mock_api_key_panel(draw, x, y, w, h):
    rounded(draw, (x, y, x + w, y + h), radius=28, fill=CARD, outline=LINE, width=3)
    draw.text((x + 28, y + 28), "Get API Key", font=font(FONT_BOLD, 36), fill=INK)
    rounded(draw, (x + 28, y + 96, x + w - 28, y + 168), radius=18, fill="#EEF6F6")
    draw.text((x + 48, y + 118), "AIzaSy••••••••••••••••", font=font(FONT_LIGHT, 30), fill=INK)
    rounded(draw, (x + 28, y + 212, x + 280, y + 286), radius=18, fill="#FFF2EE")
    draw.text((x + 62, y + 234), "Create new key", font=font(FONT_BOLD, 28), fill=ACCENT)
    for i, name in enumerate(["Google AI Studio", "Kimi 开放平台", "火山方舟"]):
        yy = y + 360 + i * 122
        rounded(draw, (x + 28, yy, x + w - 28, yy + 86), radius=18, fill="#F5F3EE")
        draw.text((x + 52, yy + 24), name, font=font(FONT_BOLD, 30), fill=INK)


def page_9():
    img, draw = page_base()
    draw.text((106, 138), "你现在先做这一件事：", font=font(FONT_BOLD, 66), fill=INK)
    lines = ["去 Google AI Studio", "或 Kimi / 火山引擎", "找到 API Key", "", "先生成一个", "保存好"]
    y = 320
    for line_text in lines:
        if line_text == "":
            y += 28
            continue
        size = 72 if line_text in {"先生成一个", "保存好"} else 54
        col = ACCENT if size > 60 else INK
        y = draw_multiline(draw, 106, y, [line_text], font(FONT_BOLD if size > 60 else FONT_LIGHT, size), fill=col, gap=20)
    paste_image_card(img, 636, 236, 474, 1120, SRC_APIKEY)
    return img


def page_10():
    img, draw = page_base()
    draw.text((106, 154), "如果你想看下一篇", font=font(FONT_BOLD, 72), fill=INK)
    draw.text((106, 296), "我可以继续整理：", font=font(FONT_LIGHT, 56), fill=MUTED)
    items = ["1. API Key 去哪里拿", "2. 哪些工具最值得接 API", "3. 怎么接最省钱"]
    y = 468
    for item in items:
        rounded(draw, (106, y, 1132, y + 150), radius=28, fill=CARD, outline=LINE, width=3)
        draw.text((144, y + 42), item, font=font(FONT_BOLD, 48), fill=INK)
        y += 188
    draw.text((106, 1318), "先收藏", font=font(FONT_BOLD, 112), fill=ACCENT)
    draw.text((106, 1454), "之后你一定会用到", font=font(FONT_LIGHT, 58), fill=INK)
    return img


PAGES = [page_1, page_2, page_3, page_4, page_5, page_6, page_7, page_8, page_9, page_10]


def make_contact_sheet(paths):
    cols = 2
    rows = math.ceil(len(paths) / cols)
    thumb_w = 360
    thumb_h = int(thumb_w * H / W)
    sheet = Image.new("RGB", (cols * thumb_w + 120, rows * thumb_h + 120), "#EFE8DD")
    draw = ImageDraw.Draw(sheet)
    for idx, path in enumerate(paths):
        img = Image.open(path).resize((thumb_w, thumb_h))
        x = 40 + (idx % cols) * (thumb_w + 40)
        y = 40 + (idx // cols) * (thumb_h + 40)
        sheet.paste(img, (x, y))
        draw.text((x, y - 28), f"Page {idx + 1}", font=font(FONT_BOLD, 24), fill=INK)
    sheet.save(OUT / "contact-sheet.png")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    paths = []
    for idx, fn in enumerate(PAGES, start=1):
        img = fn()
        path = OUT / f"api-xhs-page-{idx:02d}.png"
        img.save(path, quality=95)
        paths.append(path)
    images = [Image.open(p).convert("RGB") for p in paths]
    images[0].save(OUT / "api-xhs-pack.pdf", save_all=True, append_images=images[1:])
    make_contact_sheet(paths)
    print(f"rendered {len(paths)} pages to {OUT}")


if __name__ == "__main__":
    main()
