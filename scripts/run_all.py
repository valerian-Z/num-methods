"""一键重跑全部分析并生成图。

目标：任何时候执行 `python scripts/run_all.py`，都能从零复现 results/figures/ 下的所有图。
这是"可复现"的最低标准——别人拿到仓库，不需要问你任何问题就能跑出一样的结果。

当前状态：占位。等 numerics/integrate.py 写好后在这里串联。
"""


def main() -> None:
    print("run_all: 暂无可执行步骤")
    print("下一步 -> 在 numerics/integrate.py 中实现 trapezoid() 与 simpson()")
    print("        然后在 notebooks/01_integration.ipynb 里画误差-步长图")


if __name__ == "__main__":
    main()
