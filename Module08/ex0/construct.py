import sys
import os

os.path
sys.path


def main() -> None:
    """Entry point for the logic"""

    # Base pefix it the original prefix which the directory
    # of standard environment used to create the new env,
    #
    # prefix is the current folder that hold the python content.
    # if current == base is mean we still in standard env
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows\n")

        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct\n")

        print(f"Current Python: {sys.executable}")
        # basename is a function inside path submodule
        # which it return the last part of a path
        venv_name: str = os.path.basename(sys.prefix)
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without "
              "affecting the global system.\n")

        # Build site package path manually and print it
        print("Package installation path:")

        # Extraction python version info from the object
        major: int = sys.version_info.major
        minor: int = sys.version_info.minor
        site_packages: str = (f"{sys.prefix}/lib/"
                              f"python{major}.{minor}/site-packages")
        print(site_packages)


main()
