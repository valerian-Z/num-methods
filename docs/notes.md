# 踩坑记录

> 规则：每遇到一个 bug，记三行——报错原文 / 原因 / 解法。
> 三个月后这就是你的私人手册；复试讲"我遇到过什么问题、怎么解决的"时，素材全在这里。
> **不要只记"怎么解决的"，一定要记"为什么"。**

---

## 模板

```
### 2026-XX-XX 一句话概括问题
- 报错原文：
- 表面原因：
- 根本原因：
- 解法：
- 以后再遇到怎么快速判断：
```

---

## 2026-10-28 环境配置

### 1. `python` 命令指向 WindowsApps
- 报错原文：`where.exe python` 输出两行，第二行是 `C:\Users\dell\AppData\Local\Microsoft\WindowsApps\python.exe`
- 表面原因：PATH 里有两个 python
- 根本原因：Windows 的"应用执行别名"机制插入了 Store 占位程序
- 解法：设置 → 应用 → 高级应用设置 → 应用执行别名，关掉 `python.exe` / `python3.exe`
- 判断方法：`where.exe python` 看是否有第二行指向 WindowsApps

### 2. VSCode 打开项目后扩展全部失效
- 报错原文：`Restricted Mode is intended for safe code browsing`，右下角提示 `No Python environment extension is available`
- 根本原因：VSCode 对未信任的文件夹默认进入受限模式，禁用所有扩展
- 解法：点横幅的 `Manage` → `Trust`，然后 Reload Window
- 判断方法：标题栏是否显示 `Restricted Mode`

### 3. 把快捷键当成命令输入到终端
- 报错原文：`Ctrlr : 无法将"Ctrl"项识别为 cmdlet`
- 根本原因：`Ctrl + \`` 是键盘快捷键，不是终端命令
- 解法：用菜单 `Terminal → New Terminal`
- 教训：教程里的**反引号/尖括号包裹的内容**通常表示"按键"或"占位符"，不是要照抄的文本

---

## 2026-XX-XX （下一条从这里开始）
