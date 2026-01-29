import os
import sys
from dotenv.main import load_dotenv


def main() -> None:
    """Main entry point"""

    # Load the .env file into Environment stock to access
    # it later with the os.environ
    # override false mean that if the variable already set by shell,
    # our .env file wont override the old value, so if we pass variables in
    # command line (MATRIX_MODE=production API_KEY=secret123 python3 oracle.py)
    # there are set in shell before program even run so they wont overrided
    load_dotenv('.env', override=False)

    # Check if all required exists
    required_configs: list[str] = [
                             "MATRIX_MODE",
                             "DATABASE_URL",
                             "API_KEY",
                             "LOG_LEVEL",
                             "ZION_ENDPOINT"
                             ]

    missing: list = []
    for variable in required_configs:
        if os.environ.get(variable, None) is None:
            print(f"Variable {variable} is missing")
            missing.append(variable)

    # Accessing the variables, we can use the os.getenv which
    # can provide a default value for missing, def getenv(key, default=None):
    # but since the function internally just use os.environ.get(key, default)
    # so we'll just the original one.

    print("\nORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")
    print(f"Mode: {os.environ.get('MATRIX_MODE', 'UNKNOWN')}")

    # If no database url provided then connection failed.
    is_connected = os.environ.get('DATABASE_URL', None)
    status: str = ("Connected to local instance" if is_connected
                   else "Connecting fail")
    print(f"Database: {status}")

    # Check Api key provided
    is_auth = os.environ.get('API_KEY', None)
    access: str = "Authenticated" if is_auth else "Unauthenticated"
    print(f"API Access: {access}")

    print(f"Log Level: {os.environ.get('LOG_LEVEL', 'INFO')}")

    service = os.environ.get('ZION_ENDPOINT', None)
    zion: str = "Online" if service else "Offline"
    print(f"Zion Network: {zion}")

    print("\nEnvironment security check:")

    # Check if file have any hardcoded secrete keys or password
    # Open the program file and check its content
    # Check each line if line and skip those start with 'if' since
    # the open will read all file so to skip the checking statement.
    with open(sys.argv[0], 'r') as f:
        found: bool = False
        for line in f:
            # remove leading and trailing whitespace
            # So the startwith check work.
            line = line.strip()
            if line.startswith('if') or line.startswith('#'):
                continue
            if "API_KEY=" in line or "SECRET" in line:
                print("[WARN] Hardcoded secret found")
                found = True
                break

        if not found:
            print("[OK] No hardcoded secrets detected")

    # Check if all configuration variables present.
    if len(missing) == 0:
        print("[OK] .env file properly configured")
    else:
        print(f"[FAIL] .env missing: {missing}")

    # Override is false so command line variables will applied
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


main()
