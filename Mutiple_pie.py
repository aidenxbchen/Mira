from pyecharts import options as opts
from pyecharts.charts import Pie

# 预算数据
data = [
    ("人力成本", 20),
    ("市场成本", 20),
    ("运营成本", 10),
    ("研发成本", 50),
]

# 蓝色系（从浅到深，落在 #ebf3fe ~ #0b55b6 之间）
palette = ["#dfeafc", "#b8d2f6", "#6fa3e6", "#0b55b6"]

c = (
    Pie(init_opts=opts.InitOpts(bg_color="#ffffff", width="900px", height="560px"))
    .add(
        "",
        data,
        center=["50%", "55%"],      # 居中一点更像 PPT
        radius=["45%", "70%"],      # 做成圆环更高级、也更适合预算结构
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="预算规划",
            pos_left="center",
            title_textstyle_opts=opts.TextStyleOpts(color="#0b55b6", font_size=18),
        ),
        legend_opts=opts.LegendOpts(
            pos_left="10%",
            orient="vertical",
            textstyle_opts=opts.TextStyleOpts(color="#0b55b6"),
        ),
        tooltip_opts=opts.TooltipOpts(trigger="item"),
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(
            formatter="{b}: {c}%",
            color="#0b55b6",
            font_size=12,
        ),
    )
)

# 指定调色盘（关键：统一成蓝色系）
c.set_colors(palette)

c.render("budget_plan_pie.html")