from solution import solution


def main():
    cases = [
        ("빈 리스트", [], 10, 0),
        ("모두 기준값 미만", [1, 2, 3], 4, 0),
        ("기준값과 같은 원소", [1, 2, 3], 3, 3),
        ("중복 원소", [3, 7, 7, 2], 5, 14),
        ("음수 기준값", [-5, -2, 3], -2, 1),
        ("0 포함", [-1, 0, 1], 0, 1),
    ]

    for name, numbers, limit, expected in cases:
        original = numbers.copy()
        actual = solution(numbers, limit)
        if type(actual) is not int or actual != expected:
            raise AssertionError(f"{name}: expected={expected}, actual={actual!r}")
        if numbers != original:
            raise AssertionError(f"{name}: 입력 리스트가 변경됐어요.")

    print(f"{len(cases)}개 사례를 모두 통과했어요.")


if __name__ == "__main__":
    main()
