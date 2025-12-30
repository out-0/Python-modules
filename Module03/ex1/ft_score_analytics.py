import sys


def parse_scores() -> None:
    """Parse the provided scores and print some basic stats"""
    print("=== Player Score Analytics ===")
    # Handle No arguments
    if len(sys.argv) == 1:
        print(
                "No scores provided. "
                f"Usage: python3 {sys.argv[0]} <score1> <score2> ..."
                )
        return
    # Conver the arguments
    args = sys.argv[1:]
    valid_scores = []
    for score in args:
        try:
            valid_data = int(score)
            valid_scores.append(valid_data)
        except ValueError:
            print(f"oops, I typed ’{score}’ instead of ’1000’")

    # Check if the valid scores is 0 to avoid analytics errors
    if len(valid_scores) == 0:
        print(
                "No scores provided. "
                f"Usage: python3 {sys.argv[0]} <score1> <score2> ..."
                )
        return

    # Print the scores analytics
    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {len(valid_scores)}")
    print(f"Total score: {sum(valid_scores)}")
    print(f"Average score: {sum(valid_scores) / len(valid_scores)}")
    print(f"High score: {max(valid_scores)}")
    print(f"Low score: {min(valid_scores)}")
    print(f"Score range: {max(valid_scores) - min(valid_scores)}")
    print("")


parse_scores()
