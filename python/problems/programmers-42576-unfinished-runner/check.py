from solution import solution


def main():
    cases = [
        (["amy"], [], "amy"),
        (["ana", "bob", "ana"], ["ana", "bob"], "ana"),
        (["a", "b", "c"], ["a", "c"], "b"),
        (["kim", "kim", "kim"], ["kim", "kim"], "kim"),
        (["a", "ab", "abc"], ["abc", "ab"], "a"),
    ]
    for index, (participant, completion, expected) in enumerate(cases, start=1):
        actual = solution(participant, completion)
        if type(actual) is not str or actual != expected:
            raise AssertionError(f"사례 {index}: expected={expected!r}, actual={actual!r}")
    print(f"{len(cases)}개 로컬 사례를 모두 통과했어요.")


if __name__ == "__main__":
    main()
