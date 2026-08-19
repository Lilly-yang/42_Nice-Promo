import sys
import os
import site


print("")

# venv
if sys.prefix == sys.base_prefix:  # outside a virtual environment
    print("MATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!\n"
          "The machines can see everything you install.\n")

    print("To enter the construct, run:\n"
          "python -m venv matrix_env\n"
          "source matrix_env/bin/activate # On Unix\n"
          "matrix_env\\Scripts\\activate # On Windows\n")

    print("Then run this program again.")
else:  # inside a virtual environment
    print("MATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {sys.executable}")
    env_path = sys.prefix
    print(f"Virtual Environment: {os.path.basename(env_path)}")
    print(f"Environment Path: {env_path}\n")

    print("SUCCESS: You're in an isolated environment!\n"
          "Safe to install packages without affecting the global system.\n")

    print("Package installation path: \n"
          f"{site.getsitepackages()[0]}")


# # conda
# if os.environ.get("CONDA_PREFIX"):
#     print("Inside a Conda environment")
# else:
#     print("Outside a virtual environment")
