# 002. 기준값 이상인 숫자의 합

## 문제

정수 배열 `numbers`와 기준값 `limit`가 주어진다. `numbers`에서 `limit` 이상인 원소를 모두 더한 값을 반환한다.

- 같은 값이 여러 번 나오면 각각 더한다.
- 조건을 만족하는 원소가 없거나 배열이 비어 있으면 `0`을 반환한다.

```kotlin
class Solution {
    fun solution(numbers: IntArray, limit: Int): Int
}
```

## 예시

| numbers | limit | result |
|---|---:|---:|
| `[3, 7, 7, 2]` | 5 | 14 |
| `[1, 2, 3]` | 3 | 3 |
| `[]` | 10 | 0 |

## 제한사항

- `0 <= numbers.size <= 1,000`
- `-1,000 <= numbers[i] <= 1,000`
- `-1,000 <= limit <= 1,000`
- 반환값은 `Int` 범위 안에 있다.

## 파일

- `Solution.kt`: 직접 구현할 풀이 코드
- `Main.kt`: 첫 번째 예시 실행
- `Check.kt`: 여러 경계 사례 자동 확인

## 학습 상태

아직 풀지 않은 연습 문제다. `Solution.kt`의 `TODO`를 직접 구현한 뒤 `run`과 `check`로 확인한다.
