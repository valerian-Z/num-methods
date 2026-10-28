"""数值方法练习包。

模块划分约定：
    numerics.integrate  -- 数值积分（梯形、Simpson、高斯）
    numerics.roots      -- 方程求根（二分、牛顿、割线）
    numerics.ode        -- 常微分方程（Euler、RK4、Verlet）
    numerics.viz        -- 统一的绘图风格

写代码时遵守两条：单位写进变量名（dt_s、length_m）；参数集中放在配置里，不散落魔法数字。
"""

__version__ = "0.1.0"
