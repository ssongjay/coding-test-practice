# Python 연습

Python으로 풀 문제를 독립적으로 모으는 자리다. Kotlin 쪽 문제 번호나 내용에 맞출 필요가 없다. 현재는 아직 문제를 추가하지 않았다.

새 문제의 기본 구조:

```text
python/problems/001-example/
  README.md     # 문제 조건·입출력·제한·예시
  solution.py   # 풀이
  run.py        # 예제 입력으로 실행
  check.py      # 정상·경계 사례 검증
```

저장소 루트에서 실행한다.

```sh
./practice python 001-example run
./practice python 001-example check
```

Python 3이 필요하며 별도 빌드 단계는 없다. 실행 파일은 같은 폴더의 답안을 `from solution import solution`처럼 불러올 수 있다. 검증이 실패하면 예외 또는 0이 아닌 종료 코드를 반환한다.
