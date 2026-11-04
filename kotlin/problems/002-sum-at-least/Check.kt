private data class Case(
    val name: String,
    val numbers: IntArray,
    val limit: Int,
    val expected: Int,
)

fun main() {
    val cases = listOf(
        Case("빈 배열", intArrayOf(), 10, 0),
        Case("모두 기준값 미만", intArrayOf(1, 2, 3), 4, 0),
        Case("기준값과 같은 원소", intArrayOf(1, 3, 5), 3, 8),
        Case("중복 원소", intArrayOf(3, 7, 7, 2), 5, 14),
        Case("음수 기준값", intArrayOf(-5, -2, 3), -2, 1),
        Case("0 포함", intArrayOf(-1, 0, 1), 0, 1),
    )

    val solution = Solution()

    for (case in cases) {
        val actual = solution.solution(case.numbers, case.limit)
        check(actual == case.expected) {
            "${case.name}: expected=${case.expected}, actual=$actual"
        }
    }

    println("${cases.size}개 사례를 모두 통과했습니다.")
}
