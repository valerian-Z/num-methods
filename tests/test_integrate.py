"""数值积分的单元测试。

测试策略：优先用"解析性质"判断对错，而不是和上次结果比较。
"""

import numpy as np
import pytest

from numerics.integrate import simpson, trapezoid


def test_trapezoid_exact_for_linear() -> None:
    """梯形法对一次函数没有截断误差（f'' = 0）。

    ∫₀³ (2x + 1) dx = [x² + x]₀³ = 12
    """
    value = trapezoid(lambda x: 2.0 * x + 1.0, 0.0, 3.0, 10)
    assert value == pytest.approx(12.0, abs=1e-12)


def test_simpson_exact_for_cubic() -> None:
    """Simpson 对三次多项式精确（f'''' = 0）。

    ∫₋₁² (x³ - 2x) dx = [x⁴/4 - x²]₋₁² = 0 - (-0.75) = 0.75
    """
    value = simpson(lambda x: x**3 - 2.0 * x, -1.0, 2.0, 10)
    assert value == pytest.approx(0.75, abs=1e-12)


def test_trapezoid_rejects_invalid_n() -> None:
    """n < 1 必须报错，而不是悄悄返回 0。"""
    with pytest.raises(ValueError):
        trapezoid(np.sin, 0.0, np.pi, 0)


def test_simpson_rejects_odd_n() -> None:
    """奇数个子区间无法两两配对，必须报错。"""
    with pytest.raises(ValueError):
        simpson(np.sin, 0.0, np.pi, 9)


def _measure_order(method, f, a: float, b: float, n1: int, n2: int, exact: float) -> float:
    """用两个不同 n 的结果反推收敛阶。

    p = ln(e1 / e2) / ln(h1 / h2)
    n2 = 2 * n1 时，h1 / h2 = 2，于是 p = log₂(e1 / e2)。
    """
    h1 = (b - a) / n1
    h2 = (b - a) / n2
    e1 = abs(method(f, a, b, n1) - exact)
    e2 = abs(method(f, a, b, n2) - exact)
    return float(np.log(e1 / e2) / np.log(h1 / h2))


def test_trapezoid_is_second_order() -> None:
    """实测阶数应落在 2 附近（允许 5% 误差）。"""
    p = _measure_order(trapezoid, np.sin, 0.0, np.pi, 200, 400, 2.0)
    assert 1.9 < p < 2.1


def test_simpson_is_fourth_order() -> None:
    """实测阶数应落在 4 附近。"""
    p = _measure_order(simpson, np.sin, 0.0, np.pi, 100, 200, 2.0)
    assert 3.8 < p < 4.2
