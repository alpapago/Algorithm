class Solution {
   public int[] solution(int[] numlist, int n) {
	        for (int i = 0; i < numlist.length - 1; i++) { // numlist 탐색
	            for (int k = i + 1; k < numlist.length; k++) { // numlist 탐색(i번째 바로 이후부터)
	                int a = (numlist[i] - n) * (numlist[i] > n ? 1 : -1); // n과 numlist i번째 요소간 차이 x (1 or -1)
	                int b = (numlist[k] - n) * (numlist[k] > n ? 1 : -1); // n과 numlist k번째 요소간 차이 x (1 or -1)
	                
	                if (a > b || (a == b && numlist[i] < numlist[k])) { // n과의 차이가 작은 것에서 큰 것 순으로 numlist의 요소들을 재배열
	                    int temp = numlist[i];
	                    numlist[i] = numlist[k];
	                    numlist[k] = temp;
	                }
	            }
	        }
	        
	        return numlist; // 결과 반환(재배열 된 것)
	    }
}