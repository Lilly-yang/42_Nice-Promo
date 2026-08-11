import sys


def check_args(args: list) -> list:
    valid_args = []
    for arg in args:
        try:
            valid_args.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return valid_args


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argc = len(sys.argv)
    if argc > 1:
        valid_args = check_args(sys.argv[1:])
        valid_argc = len(valid_args)
        if valid_argc:
            print(f"Scores processed: {valid_args}")
            print(f"Total players: {valid_argc}")
            total_score = sum(valid_args)
            print(f"Total score: {total_score}")
            print(f"Average score: {total_score / valid_argc}")
            max_score = max(valid_args)
            min_score = min(valid_args)
            print(f"High score: {max_score}")
            print(f"Low score: {min_score}")
            print(f"Score range: {max_score - min_score}")
        else:
            print("No scores provided. Usage: "
                  "python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
    print("")
