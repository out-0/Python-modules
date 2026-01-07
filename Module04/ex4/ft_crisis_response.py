def crisis_handler() -> None:
    """manage different types of archive access failures"""

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print("")

    # Try file not found.
    not_exist_file = 'lost_archive.txt'
    print(f"CRISIS ALERT: Attempting access to '{not_exist_file}'...")
    try:
        with open(not_exist_file, 'r'):
            print("well, file opened successfully")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable")

    print("")
    # Try file not have permission.
    must_exist_file = 'classified_vault.txt'
    print(f"CRISIS ALERT: Attempting access to '{must_exist_file}'...")
    try:
        # Open the file with write permission,
        # but the actual file doesn't have the permission.
        with open(must_exist_file, 'w'):
            pass
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained")

    print("")
    try:
        # Try with a normal exist file
        file_name = 'standard_archive.txt'
        print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
        with open(file_name, 'r') as f:
            recovered_data = f.read()
            print(f"SUCCESS: Archive recovered - ``{recovered_data}''")
            print("STATUS: Normal operations resumed")

        print("")
        print("All crisis scenarios handled successfully. Archives secure.")
    except Exception as e:
        print(f"Well, Unexpected error : {e})")


crisis_handler()
