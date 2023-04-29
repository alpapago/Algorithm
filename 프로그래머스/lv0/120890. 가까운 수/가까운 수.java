import java.util.Arrays;

class Solution {
    public int solution(int[] array, int n) {
        Arrays.sort(array);
        for (int i = 1; i < array.length; i++) {
            if (array[i] >= n) {
                int leftValue = n - array[(i - 1)];
                int rightValue = array[i] - n;
                return leftValue <= rightValue ? array[(i - 1)] : array[i];
            }
        }
        return array[array.length - 1];
    }
}