from solution import solution


def main():
    cases = [
        (1, 0),
        (2, 2),
        (3, 2),
        (6, 12),
        (7, 12),
        (1000, 250500),
    ]
    for index, (value, expected) in enumerate(cases, start=1):
        actual = solution(value)
        if type(actual) is not type(expected) or actual != expected:
            raise AssertionError(f"사례 {index}: expected={expected!r}, actual={actual!r}")
    print(f"{len(cases)}개 로컬 사례를 모두 통과했어요.")


if __name__ == "__main__":
    main()
