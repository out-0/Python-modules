"""ft_archive_creation.py

Discovering the open file moded, and the power
of the 'w' mode, which can erase the already exist
data if not used carfuly
"""


def test_archive_creation() -> None:
    """"""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("")

    storage_name = "new_discovery.txt"
    print(f"Initializing new storage unit: {storage_name}")
    # Open file
    file = open(storage_name, 'w')
    print("Storage unit created successfully...")
    print("")
    print("Inscribing preservation data...")

    entries = [
        "{[}ENTRY 001{]} New quantum algorithm discovered",
        "{[}ENTRY 002{]} Efficiency increased by 347%",
        "{[}ENTRY 003{]} Archived by Data Archivist trainee"
    ]
    # Process the lines
    for entry in entries:
        file.write(entry + "\n")
        print(entry)

    print("")
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{storage_name}' ready for long-term preservation.")
    # Close file
    file.close()


test_archive_creation()
