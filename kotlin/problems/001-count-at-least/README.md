# 001. 기준값 이상인 숫자 개수

## 문제

정수 배열 `numbers`와 기준값 `limit`가 주어진다. `numbers`에서 `limit` 이상인 원소의 개수를 반환한다.

- 같은 값이 여러 번 나오면 각각 센다.
- 빈 배열의 결과는 `0`이다.

```kotlin
class Solution {
    fun solution(numbers: IntArray, limit: Int): Int
}
```

## 예시

| numbers | limit | result |
|---|---:|---:|
| `[3, 7, 7, 2]` | 5 | 2 |
| `[1, 2, 3]` | 3 | 1 |
| `[]` | 10 | 0 |

## 제한사항

- `0 <= numbers.size <= 1,000`
- `-1,000 <= numbers[i] <= 1,000`
- `-1,000 <= limit <= 1,000`

## 파일

- `Solution.kt`: 풀이 코드
- `Main.kt`: 첫 번째 예시 실행
- `Check.kt`: 여러 경계 사례 자동 확인

## 학습 상태

대화에서 풀이 흐름을 먼저 작성한 뒤 Kotlin 문법을 함께 고친 복습 예제다. 독립적으로 처음부터 푼 문제로 기록하지 않는다.
