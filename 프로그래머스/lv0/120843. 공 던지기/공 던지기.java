class Solution {
    public int solution(int[] numbers, int k) {
        int answer = 0;
        int idx = 0;
        for(int i=0; i<k-1;i++){ //k번 반복
            idx +=2;
            if (idx>numbers.length-1){
                idx = idx%numbers.length;
            }            
        }
        answer = numbers[idx];
        return answer;
    }
}