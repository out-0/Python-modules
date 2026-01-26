from importlib.metadata import version, PackageNotFoundError


def main():
    # Define your requirements
    dependencies: dict = {
                    'pandas': 'Data manipulation',
                    'requests': 'Network access',
                    'matplotlib': 'Visualization'
                   }

    missing_count: int = 0
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    # Map the packages names and usage of them.
    for pkg, usage in dependencies.items():
        try:
            # Get the version (this also checks if it exists)
            v: str = version(pkg)
            print(f"[OK] {pkg} ({v}) - {usage} ready")
        except PackageNotFoundError:
            # If not found, catch the error and mark as fail
            print(f"[FAIL] {pkg} (Missing) - {usage} missing")
            missing_count += 1

    if missing_count > 0:
        print(f"\n{missing_count} dependencies are missing.")
        print("For installation use: pip install -r requirements.txt")
        return

    # On SUCCESS == Only import the heavy libraries here ---
    print("\nAnalyzing Matrix data...")
    import pandas
    import matplotlib.pyplot
    import requests

    resp = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(type(resp))
    print(resp)
    print(dir(resp))
    print('')
    print('')
    print(resp.url)
    print(resp.headers)

    # Example logic:
    # df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    # print(df)

    print('')
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
