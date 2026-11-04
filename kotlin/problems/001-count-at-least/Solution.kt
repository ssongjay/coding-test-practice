class Solution {
    fun solution(numbers: IntArray, limit: Int): Int {
        var count = 0

        for (number in numbers) {
            if (number >= limit) {
                count += 1
            }
        }

        return count
    }
}
