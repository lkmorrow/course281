"""smoke_test.py 9/23/26 D. Candela
Program to test that starter environment for Physics 281 is set up
and functional.
"""
import numpy as np
from numpy import pi,sin
import scipy
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt


def main():
    print("Python environment is working")
    print("numpy:", np.__version__)
    print("scipy:", scipy.__version__)
    print("matplotlib:", matplotlib.__version__)
    print("pandas:", pd.__version__)

    x = np.linspace(0,2*pi,201)
    y = sin(x)

    data = pd.DataFrame({"x": x, "sin_x": y})

    assert len(data)==201
    assert np.isclose(data["sin_x"].iloc[0], 0.0)

    plt.figure()
    plt.plot(x, y, label="sin(x)")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.title("Physics 281 Smoke Test")
    plt.legend()
    plt.tight_layout()
    plt.savefig("smoke_test_plot.png",dpi=150)
    plt.close()

    print("Saved smoke_test_plot.png")
    print("Smoke test completed successfully")


if __name__=="__main__":
    main()
