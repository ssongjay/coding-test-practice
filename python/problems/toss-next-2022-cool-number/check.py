from solution import solution


def main():
    cases = [
        ("4555666777", 777),
        ("10002", 0),
        ("121212", -1),
        ("", -1),
        ("7", -1),
        ("77", -1),
        ("777", 777),
        ("7777", 777),
        ("999111", 999),
        ("111999", 999),
        ("000", 0),
        ("9" * 999, 999),
    ]
    for index, (s, expected) in enumerate(cases, start=1):
        actual = solution(s)
        if type(actual) is not int or actual != expected:
            raise AssertionError(f"사례 {index}: expected={expected!r}, actual={actual!r}")
    print(f"{len(cases)}개 로컬 사례를 모두 통과했어요.")


if __name__ == "__main__":
    main()
