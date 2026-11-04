# Python 연습

Python으로 풀 문제를 독립적으로 모으는 자리다. Kotlin 쪽 문제 번호나 내용에 맞출 필요가 없다.

프로그래머스에서 직접 풀고, 그 코드와 풀이 기록을 GitHub에 남긴다. 원문 링크·짧은 문제 요약·답안·검증 파일을 각 폴더에 둔다.

## 지금 풀 순서

| 순서 | 원문 | 연습할 내용 | 저장 위치 |
|---|---|---|---|
| 1 | [짝수의 합](https://school.programmers.co.kr/learn/courses/30/lessons/120831?language=python3) | 반복·조건·누적 | [120831](problems/programmers-120831-even-sum/README.md) |
| 2 | [배열 원소의 길이](https://school.programmers.co.kr/learn/courses/30/lessons/120854?language=python3) | 문자열·리스트 | [120854](problems/programmers-120854-element-lengths/README.md) |
| 3 | [같은 숫자는 싫어](https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3) | 리스트의 조건 처리 | [12906](problems/programmers-12906-no-consecutive-duplicates/README.md) |

처음 두 문제로 문법 감각을 확인한 뒤 속도와 막히는 부분에 맞춰 다음 문제를 조절한다. 세 문제 모두 아직 직접 풀이하거나 제출한 결과를 확인하지 않았다.

## 풀이 기록 흐름

1. 브라우저에 열린 프로그래머스 문제를 Python 3으로 푼다.
2. 풀이 후 코드를 저장하고, 작성 중 막힌 문법과 놓친 조건을 README에 남긴다.
3. 로컬 사례를 검증하고 프로그래머스 제출 결과는 별도로 확인한다.
4. 해당 문제의 코드와 기록을 커밋·푸시한다.

기존 자체 문제 [기준값 이상인 숫자의 합](problems/001-sum-at-least/README.md)은 보조 연습으로 남겨둔다.

새 문제의 기본 구조:

```text
python/problems/programmers-120831-even-sum/
  README.md     # 문제 조건·입출력·제한·예시
  solution.py   # 풀이
  run.py        # 예제 입력으로 실행
  check.py      # 정상·경계 사례 검증
```

저장소 루트에서 실행한다.

```sh
./practice python programmers-120831-even-sum run
./practice python programmers-120831-even-sum check
```

Python 3이 필요하며 별도 빌드 단계는 없다. 실행 파일은 같은 폴더의 답안을 `from solution import solution`처럼 불러올 수 있다. 검증이 실패하면 예외 또는 0이 아닌 종료 코드를 반환한다.
