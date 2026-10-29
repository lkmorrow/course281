"""test_smoke.py 9/23/26  D. Candela
Sample tests program for the starter Physics 281 environment, tests if
pytest is functional.
"""
import numpy as np
import pandas as pd


def test_basic_numpy_and_pandas():
    x = np.linspace(0,1,11)
    data = pd.DataFrame({"x": x, "x_squared": x**2})

    assert len(data)==11
    assert np.isclose(data["x_squared"].iloc[-1], 1.0)
