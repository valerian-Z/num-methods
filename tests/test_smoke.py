"""冒烟测试：确认包能导入、pytest 配置生效。

这个文件的价值不在于它测了什么，而在于它证明：
    1. tests/ 目录被 pytest 正确识别
    2. numerics 包在导入路径上（说明安装或目录结构没问题）
"""

import numerics


def test_package_importable() -> None:
    assert numerics.__version__ == "0.1.0"


def test_version_is_string() -> None:
    assert isinstance(numerics.__version__, str)
