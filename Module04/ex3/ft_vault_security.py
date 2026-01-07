def test_vault_security() -> None:
    """Demonstrate the 'with' statement to have a grantee
    the failsafe by the final file closing."""

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("")
    print("Initiating secure vault access...")
    with (open('classified_data.txt', 'r') as f1,
          open('security_protocols.txt', 'r') as f2):

        print("Vault connection established with failsafe protocols")
        print("")
        print("SECURE EXTRACTION:")
        # Extraction data
        data = f1.read()
        print(data)

        print("")
        print("SECURE PRESERVATION:")
        data = f2.read()
        print(data)

    print("Vault automatically sealed upon completion")
    print("")
    print("All vault operations completed with maximum security.")


test_vault_security()
