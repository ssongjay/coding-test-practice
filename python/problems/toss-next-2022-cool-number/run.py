from solution import solution


if __name__ == "__main__":
    for s in ["4555666777", "10002", "121212", ""]:
        print(f"{s!r} -> {solution(s)}")
