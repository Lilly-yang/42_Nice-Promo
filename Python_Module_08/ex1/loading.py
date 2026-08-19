import importlib


def installed_packages() -> bool:
    missing = 0
    try:
        # import pandas
        name = "pandas"
        module = importlib.import_module(name)
        print(f"[OK] {name} ({module.__version__}) - Data manipulation ready")
    except ImportError as e:
        missing = 1
        print(f"{e}")

    try:
        # import numpy
        name = "numpy"
        module = importlib.import_module(name)
        print(f"[OK] {name} ({module.__version__}) "
              "- Numerical computation ready")
    except ImportError as e:
        missing = 1
        print(f"{e}")

    # try:
    #     import requests
    #     print(f"[OK] requests ({requests.__version__}) "
    #            "- Network access ready")
    # except ImportError as e:
    #     missing = 1
    #     print(f"{e}")

    try:
        # import matplotlib
        name = "matplotlib"
        module = importlib.import_module(name)
        print(f"[OK] {name} ({module.__version__}) - Visualization ready")
    except ImportError as e:
        missing = 1
        print(f"{e}")

    if missing:
        print("\nTo install the missing dependencies, run:\n"
              " pip install -r requirements.txt  # with pip\n"
              " poetry install  # with Poetry\n")
        return False
    else:
        return True


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")
    excute = installed_packages()
    if excute:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        print("\nAnalyzing Matrix data...")
        data = np.random.rand(1000)
        print("Processing 1000 data points...")
        df = pd.DataFrame({"matrix_value": data})
        print(df.describe())
        print("Generating visualization...")
        plt.plot(df["matrix_value"])
        save_path = "matrix_analysis.png"
        plt.savefig(save_path)

        print("\nAnalysis complete!")
        print(f"Results saved to: {save_path}")
