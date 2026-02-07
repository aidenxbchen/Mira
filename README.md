# Mira · 天使轮+ 预算结构可视化（饼状图）

本仓库用于生成并展示 **Mira 天使轮+阶段的预算结构饼状图**。  
其中，`budget_plan_pie.html` 与 `index.html` 为程序输出的**图形化结果文件**，可用于融资汇报、内部讨论与网页展示。

---

## 📌 项目用途

- 将天使轮+预算分配（如研发、人力、供应链、市场等）进行结构化呈现
- 输出可直接展示的交互式饼状图（HTML）
- 支持在 GitHub Pages 上作为网页直接访问

---

## 📁 仓库文件说明

- `Mutiple_pie.py`  
  预算饼状图的生成脚本（Python）。运行后会输出图表 HTML 文件。

- `budget_plan_pie.html`  
  脚本执行后的图形化结果之一：预算饼状图页面（可直接用浏览器打开）。

- `index.html`  
  GitHub Pages 的默认入口文件。用于访问  
  `https://aidenxbchen.github.io/Mira/`  
  时直接展示图形化结果（可为同一图表或跳转到 `budget_plan_pie.html`）。

---

## 🚀 使用方法

</code>

### 1) 本地生成图表
在本地 Python 环境中运行：

```bash
python Mutiple_pie.py
```

运行完成后，会生成/更新对应的 HTML 图表文件（如 `budget_plan_pie.html`）。

### 2) 本地打开图表
生成后可直接双击 HTML 文件，或用浏览器打开：

- `budget_plan_pie.html`
- `index.html`

### 3) 在线访问（GitHub Pages）
若已开启 GitHub Pages，可直接访问：

```
https://aidenxbchen.github.io/Mira/
```

---

## 📝 说明

本仓库用于 **预算结构的沟通与表达**，便于在融资、产品与团队协作场景中快速对齐认知。  
图表结果不等同于正式财务披露文件。

---

## ✅ 上传到 GitHub（把 README 推送到仓库）

在仓库根目录执行：

```bash
git add README.md
git commit -m "Add README for angel+ budget pie chart"
git push
```