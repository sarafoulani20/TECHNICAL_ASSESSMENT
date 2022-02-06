from sys import argv
from logics import get_avg, get_count

if __name__ == '__main__':
    if len(argv) < 3:
        print("Please specify a valid action and column")
        print("Usage: python cli.py <action> <column>")
        exit(1)
    
    action = argv[1]
    column = argv[2]
    actions_map = {
        "avg": get_avg,
        "count": get_count
    }
    if action not in actions_map:
        print("Please specify a valid action")
        print("Valid actions: avg, count")
        exit(1)
    print("Running action:", action)
    print(actions_map[action](column))
    exit(0)
