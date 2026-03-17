# API图文版：普通人为什么也要懂 API

## 基本信息
- 创建日期：2026-03-15
- 目标平台：小红书
- 内容形式：图文
- 页数建议：10 页
- 目标：搜索承接 + 收藏沉淀 + 为后续 API 系列铺路
- 来源：改写自 `20260306-API科普-一根水管接三台电器.md`

## 自动路由结果（2026-03-17）
- **是否建议转图文**：建议
- **主对标**：`OpenClaw 小白科普`
- **格式借鉴说明**：借对标的页卡节奏和设计语言，不借原内容。具体保留：
  - `人群入口 -> 概念翻译 -> 类比图 -> 利益点 -> 具体场景 -> 怎么开始 -> 风险边界`
  - `类比图 / 概念对照图 / 长段文字 / 插图混排`
- **命中依据**：
  - 这条内容本身具备 `可解释 + 可拆步骤 + 可收藏` 的结构
  - 小红书实发数据已经验证 `API` 有收藏承接：`1,736` 观看、`132` 收藏、收藏率 `7.6%`
  - 适合继续做 `API 入门 -> API Key 获取 -> 常用工具接入` 的系列链路

## 这篇图文的核心逻辑
这不是一篇给程序员看的技术教程，而是一篇给普通用户看的“认知升级 + 低门槛启蒙”图文。

小红书上这类内容要成立，必须同时满足 3 个条件：
1. **标题能被搜到，也能被点开**：用户要一眼知道这是在讲什么
2. **前 3 页就把复杂概念讲简单**：不能像视频一样靠口播节奏带着走
3. **后面要给明确场景和动作**：不然用户会觉得“听懂了，但不知道怎么开始”

所以这篇图文的结构不是“先讲概念再举例”，而是：
- 先告诉用户这件事和他有关系
- 再用一个极简比喻讲明白
- 然后立刻给 3 个场景
- 最后给一个能马上执行的动作

## 发布目标与判断标准
- **主要目标**：搜索 + 收藏
- **次要目标**：评论区追问下一篇（API Key 获取 / 接入教程）
- **达标标准**：
  - 内容点击率 > 10%
  - 收藏 > 50
  - 评论区出现明确追问：`怎么获取` / `怎么接` / `哪些工具值得接`

## 标题方案

### 主标题（推荐）
普通人为什么一定要懂 API？一篇讲明白

### 备选标题
1. API 到底是什么？我用一根水管讲清楚
2. 为什么懂 API 的人，同样预算能多用 3 倍工具
3. 不会 API，你会一直在为 AI 套壳付钱

## 封面方案

### 封面文案（推荐）
- 主标题：普通人为什么也要懂 API
- 副标题：一根水管，接活 3 个 AI 工具
- 角标：Claude Code / OpenClaw / 翻译插件

### 封面排版
- 尺寸：`3:4` 竖版
- 画面结构：
  - 上半区放主标题，左对齐
  - 中间放“水管分流”主视觉
  - 下半区放 3 个工具卡片，形成“一个能力接多个工具”的感觉
- 文案层级：
  - 主标题最大
  - 副标题次之
  - 角标只做补充，不要抢主标题注意力

### 封面视觉风格
- 背景：奶油白或浅灰白，避免纯白太空
- 主色：深灰黑 + 番茄红点题
- 辅助色：低饱和蓝绿色，强化“技术感”
- 风格关键词：干净、编辑感、信息图、不是电商风

### 封面图生成提示词
先用 AI 生背景和主体结构，文字后期手动加，不要让 AI 直接生成中文字。

```text
vertical 3:4 editorial infographic cover, cream background, a central water pipe branching into three devices, one coding laptop, one autonomous assistant dashboard, one browser translation panel, clean minimal tech education style, modern flat illustration, subtle grid, high contrast, red accent, dark charcoal lines, premium Xiaohongshu editorial design, no text, no watermark
```

## 统一排版规则

### 尺寸与安全区
- 画布：`1242 x 1660` 或任意 `3:4` 比例
- 四周安全边距：至少 `90px`
- 每页正文不超过 `6` 行
- 每行尽量控制在 `12-18` 个汉字内

### 字体和层级
- 主标题：粗黑体，强调词单独换色
- 正文：中黑或常规黑体，保证手机端扫读清楚
- 强调词：只高亮 1-2 个，不要整页满屏高亮

### 小红书图文创作逻辑
- 第 1 页负责 **点击后不退出**
- 第 2-3 页负责 **把门槛打掉**
- 第 4-7 页负责 **给用户具体价值感**
- 第 8-9 页负责 **形成记忆点和行动指令**
- 第 10 页负责 **评论和收藏 CTA**

## 制作顺序
1. 先做封面和第 3 页“水厂-水管-电器”核心解释图
2. 再做第 5-7 页三个案例页
3. 最后补第 2、4、8、9、10 页的文字卡页
4. 全部页卡完成后，再写正文和标签
5. 发布前检查首页、最后一页、正文开头是否同一逻辑链路

## 真实截图补充清单（2026-03-17 核对）

这篇图文不是必须全用 AI 图。能上真实截图的地方，优先上真实截图。

### 截图优先级
1. **优先截图**：官方控制台、工具设置页、插件配置页、GitHub 项目页
2. **次优先截图**：你自己的实际使用界面
3. **最后才用 AI 图**：类比图、概念示意图、封面底图

### 建议截图位

#### A. Google AI Studio / Gemini API
- **用途**：支撑第 9 页“先生成一个 API Key”
- **建议截图内容**：
  - Google AI Studio 首页的 `Get a Gemini API Key`
  - API Keys 页面
  - 创建完成后的 key 列表页
- **建议搜索/打开目标**：
  - [Google AI Studio](https://ai.google.dev/aistudio)
  - [Using Gemini API keys](https://ai.google.dev/tutorials/setup)

#### B. Kimi 开放平台
- **用途**：支撑第 9 页“不是只有 Google 才能拿 Key”
- **建议截图内容**：
  - `账户总览`
  - `API Key 管理`
  - `新建 API Key`
- **建议搜索/打开目标**：
  - [Kimi API 快速入门](https://platform.moonshot.cn/blog/posts/kimi-api-quick-start-guide)

#### C. 火山方舟
- **用途**：支撑第 9 页“国内平台也能拿 Key”
- **建议截图内容**：
  - `获取 API Key 并配置`
  - 控制台中的 API Key 管理页
- **建议搜索/打开目标**：
  - [获取 API Key 并配置](https://www.volcengine.com/docs/82379/1541594)

### 这篇里每一页的素材优先级
- **第 1 页**：AI 图
- **第 2 页**：纯文字
- **第 3 页**：AI 图
- **第 4 页**：纯文字
- **第 5 页**：真实截图优先，Claude Code / 终端界面
- **第 6 页**：真实截图优先，OpenClaw / GitHub / 控制台界面
- **第 7 页**：真实截图优先，沉浸式翻译插件配置页
- **第 8 页**：纯文字或轻图标
- **第 9 页**：真实截图优先，官方 API Key 页面
- **第 10 页**：纯文字

---

## 逐页执行包

### 第 1 页：封面
**目标**：建立搜索意图和学习预期

**页面文案**：
```text
普通人为什么
也要懂 API

一根水管
接活 3 个 AI 工具
```

**排版说明**：
- 主标题分两行，增强停留感
- “API” 单独高亮
- 副标题更小，放在下方承接，不要和主标题抢层级

**配图方式**：AI 生成背景 + 后期手动排字

**Canva 操作要求**：
- 用 `3:4` 画布
- 主标题放左上，分两行
- `API` 用强调色
- 中间水管图占页面中轴，不要偏上
- 底部副标题和 3 个工具角标做次级信息

**图片生成提示词**：
```text
vertical 3:4 editorial infographic cover, cream background, one central blue-green water pipe splitting into three branches, three generic tech devices around it, coding laptop, agent dashboard, browser translation window, clean premium editorial style, simple geometric shapes, subtle red accent, modern Chinese social media visual, no text, no logo, no watermark
```

### 第 2 页：痛点页
**目标**：让用户立刻觉得“这件事和我有关”

**页面文案**：
```text
很多人不是不会用 AI

而是不会接自己的 API

所以只能一直用
别人套好壳的版本

功能更少
价格还更贵
```

**排版说明**：
- 纯文字卡页即可
- “不会接自己的 API” 单独加粗放大
- 底部可以放一行小字：`这就是很多人卡住的地方`

**配图方式**：不需要生成图片，文字卡即可

**Canva 操作要求**：
- 左上对齐，不居中
- 第 2 行 `不会接自己的 API` 字号最大
- 底部留一段空白，不要把文字塞满

### 第 3 页：核心解释图
**目标**：10 秒讲明白 API 是什么

**页面文案**：
```text
AI 公司 = 自来水厂
API = 你家的水管
工具 = 洗衣机 / 花洒 / 洗碗机

你买的不是某个工具
而是“水”
接到哪里，由你决定
```

**排版说明**：
- 这一页必须做成图解，不要只放文字
- 画面中间是一根主水管，分出 3 个支路
- 每个支路连接一个工具图标或界面示意

**配图方式**：AI 生成信息图底图 + 手动排字

**Canva 操作要求**：
- 顶部放 `AI公司 / API / 工具` 三层对应关系
- 中间主水管必须贯穿全页
- 三个分支尽量左右下均衡展开
- 每个分支只配一个图标或一个界面框，不要堆太多图

**图片生成提示词**：
```text
vertical 3:4 clean infographic, central water factory icon on top, one main pipe flowing down and branching into three devices, one laptop for coding, one assistant dashboard, one browser translation panel, minimal editorial diagram style, cream background, dark lines, muted teal and tomato red accents, clean modern tech illustration, no text, no watermark
```

### 第 4 页：利益点页
**目标**：把抽象概念转成普通人能理解的好处

**页面文案**：
```text
懂 API
不是让你变程序员

而是让你可以：

更省钱
接更多工具
不被单个平台绑死
```

**排版说明**：
- 纯文字卡页
- `更省钱 / 接更多工具 / 不被绑死` 做成 3 个并列 bullet
- 每个 bullet 控制在 4-6 个字

**配图方式**：不需要生成图片，文字卡即可

**Canva 操作要求**：
- 主标题放上半区
- 下半区做 3 个 bullet 小模块
- 每个利益点前放一个极简图标即可

### 第 5 页：案例 1 - Claude Code
**目标**：讲“省钱 + 灵活”

**页面文案**：
```text
案例 1：Claude Code

接自己的 API 后
后台跑什么模型
你自己决定

不一定非得买原生订阅
成本会更可控
```

**排版说明**：
- 左侧放 5 行文案
- 右侧放一个“代码界面/终端”视觉
- 不要强行生成品牌 Logo，保持通用工具感

**推荐素材**：真实截图优先；没有截图再用 AI 图

**建议截图位**：
- Claude Code 终端窗口
- 模型/Provider 配置位
- 代码生成中的操作界面

**Canva 操作要求**：
- 左 40% 放文字，右 60% 放截图
- 截图外加细边框，不要裸贴
- 页面右下角补一行小字：`同样是 coding，底层模型你自己选`

**图片生成提示词（无截图时用）**：
```text
vertical 3:4 clean tech card, modern coding workspace, laptop screen with terminal and code blocks, premium editorial style, cream background, subtle teal and charcoal palette, minimal interface details, no text, no logo, no watermark
```

### 第 6 页：案例 2 - OpenClaw
**目标**：讲“很多开源工具需要你自己接模型”

**页面文案**：
```text
案例 2：OpenClaw

很多开源工具
本身不送模型

你要自己把 API 接进去
它才真正活过来
```

**排版说明**：
- 左上角放标题
- 中间放“机器人控制台/多平台联动”的视觉
- 底部放一句补刀：`不会 API，就只能看别人用`

**推荐素材**：GitHub 页面或工具界面截图优先

**建议截图位**：
- GitHub 项目主页
- OpenClaw 配置界面
- “需要接模型”相关设置页

**Canva 操作要求**：
- 上半区标题 + 一句话判断
- 中段放截图
- 底部单独放：`不会 API，就只能看别人用`

**图片生成提示词（无截图时用）**：
```text
vertical 3:4 editorial tech illustration, autonomous assistant control dashboard, robot assistant concept, multi-platform workflow panels, modern UI cards, clean cream background, muted teal, charcoal and red accents, premium informative social post style, no text, no logo, no watermark
```

### 第 7 页：案例 3 - 沉浸式翻译
**目标**：讲“效果提升”

**页面文案**：
```text
案例 3：沉浸式翻译

免费版能用
但质量一般

接上自己的 API Key 后
调用的是你选的大模型
翻译质量会明显更好
```

**排版说明**：
- 左侧文案，右侧浏览器翻译界面示意
- 关键词 `API Key` 和 `大模型` 做高亮

**推荐素材**：浏览器插件设置页截图优先

**建议截图位**：
- 沉浸式翻译设置页
- 模型/API Key 配置位
- 翻译前后效果对照

**Canva 操作要求**：
- 左侧文案，右侧截图
- `API Key` 和 `大模型` 单独高亮
- 可以加一个极细的“免费版 vs 自定义模型”对照标签

**图片生成提示词（无截图时用）**：
```text
vertical 3:4 browser translation interface concept, bilingual text blocks, side-by-side translation window, clean minimal editorial tech style, cream background, dark charcoal text placeholders, muted blue-green accents, premium Chinese social media infographic look, no real text, no logo, no watermark
```

### 第 8 页：记忆点总结
**目标**：把全篇收成一句话

**页面文案**：
```text
一根水管
接了三台电器

一个编程工具
一个 AI 助手
一个翻译插件

这就是 API
最值得普通人理解的地方
```

**排版说明**：
- 居中排版
- 第一行和第二行做最大字号
- 下半区可以用 3 个小图标辅助，不需要复杂配图

**配图方式**：轻图标或纯文字卡均可

**Canva 操作要求**：
- 全页居中
- 第一句 `一根水管` 最大
- 三个工具名称可以做成三列小标签

### 第 9 页：行动步骤
**目标**：给用户一个零门槛起步动作

**页面文案**：
```text
你现在先做这一件事：

去 Google AI Studio
或 Kimi / 火山引擎
找到 API Key

先生成一个
保存好
```

**排版说明**：
- 用清单式排版
- “先生成一个，保存好” 单独放大
- 这一页必须让用户感觉“我今天就能做”

**配图方式**：真实截图优先；没有再退回纯文字卡

**建议截图位**：
- Google AI Studio `Get API Key`
- Kimi `API Key 管理`
- 火山方舟 `获取 API Key 并配置`

**Canva 操作要求**：
- 左侧放步骤
- 右侧放 1 张官方页截图
- 如果一页塞不下 3 个平台，只保留 Google AI Studio 这一张截图，其他两个写进正文

### 第 10 页：评论与收藏 CTA
**目标**：拉动互动，并给下一篇预埋需求

**页面文案**：
```text
如果你想看下一篇

我可以继续整理：
1. API Key 去哪里拿
2. 哪些工具最值得接 API
3. 怎么接最省钱

先收藏
之后你一定会用到
```

**排版说明**：
- 用列表排版，增强“系列感”
- 最后一行 `先收藏` 做最大强调

**配图方式**：纯文字卡页即可

**Canva 操作要求**：
- 先放 `如果你想看下一篇`
- 中间 3 个选项做编号列表
- `先收藏` 放页面最底部，单独放大

---

## 正文文案（可直接发）

```text
很多人以为 API 是程序员才需要懂的东西。
但我这次越来越强烈地感觉到，普通人也很有必要知道 API 是什么。

因为你一旦理解它，你会发现：
你买的不是某个 AI 工具，
你买的是一根可以接到很多工具上的“水管”。

Claude Code 可以接，
OpenClaw 这种开源工具可以接，
沉浸式翻译这种插件也可以接。

不会 API，你就只能一直用别人套好壳的版本；
会 API，同样预算下，你能用的工具会多很多。

这篇我先把 API 的底层逻辑讲明白。
如果你想看下一篇，我可以继续写：
1. API Key 到底去哪里拿
2. 哪些普通人常用工具最值得接 API
3. 怎么接最省钱

你现在先收藏，后面一定会用到。
```

## 置顶评论文案

```text
下一篇你们更想看哪个：
1. API Key 到底去哪里拿
2. 哪些工具接 API 最值
3. 新手第一次接 API 怎么不踩坑
```

## 标签建议
- #AI
- #API
- #AI工具
- #ClaudeCode
- #OpenClaw
- #沉浸式翻译
- #效率工具
- #AI入门

## 正文第一句备选

发的时候，正文开头优先用下面这句，不要换成太虚的开场：

```text
很多人以为 API 是程序员才需要懂的东西，但普通人越早理解 API，越容易少花冤枉钱。
```

## 下一篇承接建议

这篇发完后，如果评论区有人问“怎么拿”，下一篇就直接做：

`API Key 到底去哪里拿？Google / Kimi / 火山方舟一篇讲明白`

这样承接最自然，因为：
- 这篇已经把“为什么要懂”讲完了
- 下一篇只需要回答“第一步怎么做”
- 用户评论区会天然给你需求

## 发布时间建议
- **优先时段**：工作日 `12:00-13:30` 或 `18:30-21:00`
- **原因**：这篇属于“学习型 + 收藏型”内容，更适合用户有主动阅读时间的窗口

## 发布前检查清单
- [ ] 封面是否只保留一个主问题，不堆词
- [ ] 第 3 页的“水厂-水管-电器”图是不是一眼能懂
- [ ] 第 5-7 页是否都落在“一个案例 = 一个具体价值”
- [ ] 所有页卡单页文字是否可在 3 秒内扫完
- [ ] AI 生成图是否都没有乱码文字；有的话一律后期手动排字
- [ ] 正文第一句是否能直接承接封面，不要换话题
- [ ] 最后一页和正文是否都在引导“收藏 + 评论区追问下一篇”

## 你现在的最优执行顺序
1. 先做封面图和第 3 页核心解释图
2. 再做第 5、6、7 页三个案例页
3. 然后补文字卡页（2、4、8、9、10）
4. 全部做完后，把正文和置顶评论一起准备好
5. 发布后重点盯：点击率、收藏、评论区追问方向
