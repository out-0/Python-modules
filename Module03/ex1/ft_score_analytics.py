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
    valid_scores = [None] * 100
    index = 0
    for score in args:
        try:
            valid_data = int(score)
            valid_scores[index] = (valid_data)
            index += 1
        except ValueError:
            print(f"oops, I typed ’{score}’ instead of ’1000’")

    # Check if the valid scores is 0 to avoid analytics errors
    if len(valid_scores) == 0:
        print(
                "No scores provided. "
                f"Usage: python3 {sys.argv[0]} <score1> <score2> ..."
                )
        return
    # Remove the None's from the static list and convert it to a exact length
    length = 0
    for score in valid_scores:
        if score is not None:
            length += 1
    valid_scores_list = [None] * length
    index = 0
    while index < length:
        valid_scores_list[index] = valid_scores[index]
        index += 1

    # Print the scores analytics
    print(f"Scores processed: {valid_scores_list}")
    print(f"Total players: {len(valid_scores_list)}")
    print(f"Total score: {sum(valid_scores_list)}")
    print(f"Average score: {sum(valid_scores_list) / len(valid_scores_list):.1f}")
    print(f"High score: {max(valid_scores_list)}")
    print(f"Low score: {min(valid_scores_list)}")
    print(f"Score range: {max(valid_scores_list) - min(valid_scores_list)}")
    print("")


parse_scores()
