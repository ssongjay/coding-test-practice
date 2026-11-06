from solution import solution


def main():
    cases = [
        (["amy"], [], "amy"),
        (["ana", "bob", "ana"], ["ana", "bob"], "ana"),
        (["a", "b", "c"], ["a", "c"], "b"),
        (["kim", "kim", "kim"], ["kim", "kim"], "kim"),
        (["a", "ab", "abc"], ["abc", "ab"], "a"),
        (["ana", "bob", "cy"], ["ana", "bob"], "cy"),
        (["ana", "ana", "bob"], ["ana", "ana"], "bob"),
        (["a" * 20, "b" * 20], ["b" * 20], "a" * 20),
        (["kim"] * 100_000, ["kim"] * 99_999, "kim"),
    ]
    # 소문자 네 자리로 서로 다른 이름 100,000개를 만든다.
    names = [
        "".join(chr(ord("a") + (number // (26 ** position)) % 26) for position in range(4))
        for number in range(100_000)
    ]
    missing = 50_000
    cases.append((names, list(reversed(names[:missing] + names[missing + 1:])), names[missing]))
    for index, (participant, completion, expected) in enumerate(cases, start=1):
        original_participant = participant.copy()
        original_completion = completion.copy()
        actual = solution(participant, completion)
        if participant != original_participant or completion != original_completion:
            raise AssertionError(f"사례 {index}: 입력 리스트가 변경됐어요.")
        if type(actual) is not str or actual != expected:
            raise AssertionError(f"사례 {index}: expected={expected!r}, actual={actual!r}")
    print(f"{len(cases)}개 로컬 사례를 모두 통과했어요.")


if __name__ == "__main__":
    main()
