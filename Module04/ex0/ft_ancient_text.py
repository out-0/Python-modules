def test_recovery_system() -> None:
    """Structure the recovery system"""

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("")

    # Opening the file
    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...")
    try:
        vault = open('ancient_fragment.txt', 'r')
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
        return
    print("")

    # Read and print data
    print("RECOVERED DATA:")
    text = vault.read()
    print(text)
    print("")

    # Close the file
    vault.close()
    print("Data recovery complete. Storage unit disconnected.")


test_recovery_system()
