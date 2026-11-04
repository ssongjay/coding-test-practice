# coding-test-practice

언어별로 분리해 관리하는 코딩테스트 연습 기록. 현재는 Python 기본 문법을 복습하고 있다. Kotlin과 Python의 문제는 독립적으로 관리한다.

## 시작하기

### Python 연습

프로그래머스에서 문제를 풀고, 작성한 코드와 풀이 기록을 GitHub에 정리한다. 첫 문제는 [짝수의 합](https://school.programmers.co.kr/learn/courses/30/lessons/120831?language=python3)이다. [Python 문제 목록](python/README.md) 순서대로 진행한다.

```sh
./practice python programmers-120831-even-sum run
./practice python programmers-120831-even-sum check
```

프로그래머스에서 푼 코드를 해당 문제 폴더의 `solution.py`에 기록하고 로컬 사례도 확인한다. 답안 작성 전에는 미구현 오류가 난다. 로컬 검증 결과와 플랫폼 제출 결과를 구분하고, 풀이 후 변경은 커밋·푸시한다.

### Kotlin 연습

Kotlin 실행에는 JDK 17이 필요하다. Gradle과 Kotlin 컴파일러는 Wrapper가 준비하므로 별도로 설치할 필요가 없다. 첫 실행에는 다운로드를 위한 인터넷 연결이 필요할 수 있다.

macOS에서 시스템에 등록된 JDK 17 또는 Homebrew의 `openjdk@17`을 설치해두면 `practice`가 찾아서 사용한다. 다른 위치의 JDK는 `JAVA_HOME`으로 지정한다. IntelliJ에서는 `kotlin/` 폴더를 Gradle 프로젝트로 열고 Gradle JVM을 JDK 17로 선택한다.

저장소 루트에서 실행한다.

```sh
# 함께 확인한 첫 예제 실행: 2 출력
./practice kotlin 001-count-at-least run

# 정상·경계 사례를 한 번에 검증
./practice kotlin 001-count-at-least check

# 다음 문제의 문법·타입 검사
./practice kotlin 002-sum-at-least build
```

이어서 [002 — 기준값 이상인 숫자의 합](kotlin/problems/002-sum-at-least/README.md)을 읽고 그 폴더의 `Solution.kt`를 작성한다. `TODO`를 채우기 전에는 run·check가 실패한다. 컴파일 성공은 정답이라는 뜻이 아니다.

## 폴더 구조

```text
kotlin/
  build.gradle.kts
  settings.gradle.kts
  gradlew
  gradle/wrapper/
  problems/
    001-count-at-least/
      README.md          # 문제
      Solution.kt        # 답안 작성 위치
      Main.kt            # 예제 실행
      Check.kt           # 정상·경계 사례 검증
    002-sum-at-least/
      README.md
      Solution.kt
      Main.kt
      Check.kt
python/
  README.md
  problems/
    001-sum-at-least/
      README.md
      solution.py
      run.py
      check.py
practice                 # 언어·문제·실행 방식을 선택하는 명령
```

| 언어 | 문제 | 상태 |
|---|---|---|
| Kotlin | [001 — 기준값 이상인 숫자의 개수](kotlin/problems/001-count-at-least/README.md) | 함께 문법을 확인한 예제 |
| Kotlin | [002 — 기준값 이상인 숫자의 합](kotlin/problems/002-sum-at-least/README.md) | 직접 구현 전 |
| Python | [001 — 기준값 이상인 숫자의 합](python/problems/001-sum-at-least/README.md) | 직접 구현 전 |
| Python | [프로그래머스 — 짝수의 합](python/problems/programmers-120831-even-sum/README.md) | 현재 시작점 |
| Python | [프로그래머스 — 배열 원소의 길이](python/problems/programmers-120854-element-lengths/README.md) | 다음 문제 |
| Python | [프로그래머스 — 같은 숫자는 싫어](python/problems/programmers-12906-no-consecutive-duplicates/README.md) | 이후 문제 |

자체 연습 문제와 출처를 표시한 프로그래머스 문제를 함께 보관한다. 새 문제는 각 언어의 `problems/<번호-이름>/`에 추가한다. 문제 이름은 영문 소문자·숫자·하이픈을 사용한다.

## 실행과 검증의 차이

- **build:** 선택한 문제의 Kotlin 파일을 컴파일해 문법·타입 오류를 확인한다.
- **run:** `Main.kt`의 예제 입력을 답안에 전달해 결과를 출력한다.
- **check:** `Check.kt`가 빈 배열·경계값·중복·음수 등 지정된 입력의 실제 결과를 기대값과 비교한다. 다르면 실패 종료한다.

지정한 사례를 통과해도 모든 가능한 입력을 검증한 것은 아니다. 입력 크기와 시간복잡도를 설명하고, 새 반례를 발견하면 해당 문제의 Check.kt에 추가한다. 플랫폼에 제출할 때는 요구한 함수 형태에 맞춰 Solution.kt의 답안을 사용한다.

Kotlin은 선택한 문제 폴더 하나만 컴파일하므로 각 문제에 같은 이름의 `Solution` 클래스와 `main` 함수를 둘 수 있다. 다른 문제를 풀 때 파일을 옮길 필요 없이 실행 명령의 문제 이름을 바꾼다.

Gradle을 직접 사용하려면 `kotlin/` 안에서 실행한다.

```sh
cd kotlin
./gradlew -Pproblem=001-count-at-least runSolution
./gradlew -Pproblem=001-count-at-least checkSolution
./gradlew -Pproblem=001-count-at-least build
```

직접 Wrapper를 실행할 때는 JDK 17이 검색 가능한 환경이어야 한다. `gradlew build`에는 사례 검증도 포함되고, 루트의 `practice ... build`는 연습 중 문법만 확인하려는 용도로 컴파일만 한다.

## Python을 추가할 때

`python/problems/<번호-이름>/` 안에 `README.md`, `solution.py`, `run.py`, `check.py`를 둔다. Kotlin 쪽과 독립적인 문제를 추가한다.

```sh
# 해당 Python 문제 파일을 만든 뒤, 저장소 루트에서 실행
./practice python 001-example run
./practice python 001-example check
```

Python 3만 있으면 별도 빌드 없이 실행한다. 자세한 파일 역할은 [Python 안내](python/README.md)에 적었다.

## Kotlin은 프로젝트 없이도 실행할 수 있나

가능하다. JDK와 `kotlinc`가 설치돼 있다면 문제 폴더에서 다음처럼 컴파일하고 실행할 수 있다.

```sh
kotlinc Solution.kt Main.kt -include-runtime -d practice.jar
java -jar practice.jar
```

실행을 시작할 `main` 함수가 필요하다. Solution.kt에 풀이 클래스만 있다면 호출할 Main.kt도 함께 컴파일한다. 이 저장소에서는 컴파일러 버전과 문제 선택을 맞추기 위해 Gradle Wrapper를 사용한다. 코딩테스트 플랫폼에서는 준비된 호출부에 맞춰 답안 함수만 작성하는 경우도 있다.

## Kotlin 연습 환경

- Kotlin/JVM 2.2.21
- JDK 17
- Gradle Wrapper 8.13
- 별도 테스트 프레임워크 없이 Kotlin 표준 라이브러리의 `check`로 사례 확인

이 버전은 로컬 연습 환경이다. 실제 시험의 허용 언어·컴파일러·런타임은 시험 안내에서 따로 확인한다.
