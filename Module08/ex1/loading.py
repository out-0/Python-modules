from importlib.metadata import version, PackageNotFoundError


def main() -> None:
    """Main entry point"""

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
            # using version method from metadata
            v: str = version(pkg)
            print(f"[OK] {pkg} ({v}) - {usage} ready")
        except PackageNotFoundError:
            # If not found, catch the error and mark as fail
            print(f"[FAIL] {pkg} (Missing) - {usage} missing")
            missing_count += 1

    if missing_count > 0:
        print(f"\n{missing_count} dependencies are missing.")
        print("For installation:\n")
        print("--: Using pip:\n")
        print("pip install -r requirements.txt\n")
        print("--: Using poetry:\n")
        print("poetry env activate")
        print("source /home/your_user/.cache/pypoetry/virtualenvs/"
              "ex1-BvIkvnFx-py3.14/bin/activate")
        print("poetry install")
        return

    # On SUCCESS == Only import the heavy libraries here ---
    print("\nAnalyzing Matrix data...")
    import pandas
    import matplotlib.pyplot as plt
    import requests

    resp = requests.get("https://jsonplaceholder.typicode.com/posts")
    # Check if the request fail or not.
    try:
        if resp.status_code >= 404:
            raise Exception("HTTP error: Data fetching fail")
    except Exception as e:
        print(e)

    # Extract the json data (decoding the bytes content into json structure)
    json_data: list[dict] = resp.json()

    print("Processing 1000 data points...")
    # Covert that json data to a convenient structural data sheet
    pandas_format = pandas.DataFrame(json_data)

    print("Generating visualization...")
    # Extract numerical columns since plot
    # can't operate on sentence (strings) columns
    # User double list to extract a DataFrame(2D) formate instead of series(1D)
    numberical_columns = pandas_format[['id', 'userId']]

    # Draw the visualization in its memory space place
    numberical_columns.plot()

    print('')
    print("Analysis complete!")
    # Save the visualization as png picture.
    plt.savefig('matrix_analysis.png')
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
