"""数值积分：复合梯形法与复合 Simpson 法。

两个函数的共同目标是"可被收敛阶检验"：
步长减半时，误差应分别下降为 1/4 和 1/16。

本模块只做数值计算，不做绘图、不读文件。
"""

from collections.abc import Callable

import numpy as np


def trapezoid(
    f: Callable[[np.ndarray], np.ndarray],
    a: float,
    b: float,
    n: int,
) -> float:
    """复合梯形公式。

    Parameters
    ----------
    f : callable
        被积函数，接受 ndarray 返回 ndarray（支持向量化）。
    a, b : float
        积分区间端点，要求 a < b。
    n : int
        子区间数，必须 >= 1。

    Returns
    -------
    float
        积分近似值。

    Raises
    ------
    ValueError
        当 n < 1 时。
    """
    if n < 1:
        raise ValueError(f"n 必须 >= 1，收到 {n}")

    x = np.linspace(a, b, n + 1)
    y = f(x)

    h = (b - a) / n
    return float(h * (0.5 * y[0] + y[1:-1].sum() + 0.5 * y[-1]))


def simpson(
    f: Callable[[np.ndarray], np.ndarray],
    a: float,
    b: float,
    n: int,
) -> float:
    """复合 Simpson 公式（n 必须为偶数）。

    在参数、返回值和异常行为上与 trapezoid 保持一致，
    以便两者可以直接对比。
    """
    if n < 2 or n % 2 != 0:
        raise ValueError(f"n 必须为 >= 2 的偶数，收到 {n}")

    x = np.linspace(a, b, n + 1)
    y = f(x)

    h = (b - a) / n
    return float(h / 3 * (y[0] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum() + y[-1]))

