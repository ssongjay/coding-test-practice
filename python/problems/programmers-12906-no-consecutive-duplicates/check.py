from solution import solution


def main():
    cases = [
        ([1], [1]),
        ([2, 2, 2], [2]),
        ([1, 2, 1], [1, 2, 1]),
        ([0, 0, 9, 9, 0], [0, 9, 0]),
        ([9, 8, 8, 7], [9, 8, 7]),
    ]
    for index, (value, expected) in enumerate(cases, start=1):
        actual = solution(value)
        if type(actual) is not type(expected) or actual != expected:
            raise AssertionError(f"사례 {index}: expected={expected!r}, actual={actual!r}")
    print(f"{len(cases)}개 로컬 사례를 모두 통과했어요.")


if __name__ == "__main__":
    main()
