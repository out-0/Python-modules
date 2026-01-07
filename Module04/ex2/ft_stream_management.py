from sys import stdin, stderr, stdout

"""ft_stream_management.py

Handles the three sacred data channels of the Cyber Archives.
Collects archivist ID and status reports, routes messages to stdout
and stderr appropriately, and demonstrates proper stream separation.
"""


def test_stream_management() -> None:
    """Test the 3 standard files for streaming data"""

    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print("")

    # Dimonstraite input buffer
    # Removing newline stop the auto flashing
    print("Input Stream active. Enter archivist ID: ", end="")
    # Flashing stdout buffer manually
    stdout.flush()
    # Removing the new line at the end for clean printing later.list
    # since readline read also the [enter] new line.
    archivist_id = stdin.readline()[:-1]

    print("Input Stream active. Enter status report: ", end="")
    stdout.flush()
    status_report = stdin.readline()[:-1]

    print("")

    stdout.write(f"[STANDARD] Archive status from "
                 f"{archivist_id}: {status_report}\n")
    stderr.write("[ALERT] System diagnostic: "
                 "Communication channels verified\n")
    stdout.write("[STANDARD] Data transmission complete\n")

    print("")
    print("Three-channel communication test successful.")


test_stream_management()
