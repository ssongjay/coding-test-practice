from solution import solution


def main():
    cases = [
        (['a', 'Ab!'], [1, 3]),
        (['cat'], [3]),
        (['xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'], [100]),
        (['!', 'Hi!'], [1, 3]),
        (['a', 'b', 'c'], [1, 1, 1]),
    ]
    for index, (value, expected) in enumerate(cases, start=1):
        actual = solution(value)
        if type(actual) is not type(expected) or actual != expected:
            raise AssertionError(f"사례 {index}: expected={expected!r}, actual={actual!r}")
    print(f"{len(cases)}개 로컬 사례를 모두 통과했어요.")


if __name__ == "__main__":
    main()
