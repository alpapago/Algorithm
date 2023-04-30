class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        
        if(num%2!=0){
            int mid = (num-1)/2;
            int midv = total/num;
            answer[mid] = midv;
            for(int i=1;i<=(num-1)/2;i++){
                answer[mid-i] = midv-i;
                answer[mid+i] = midv+i;
            }
        }else{
            int midl = num/2-1;
            int midr = num/2;
            int midv = (total/(num/2))/2;
            answer[midl] = midv;
            answer[midr] = midv+1;
            for(int i=1;i<num/2;i++){
                answer[midl-i] = answer[midl]-i;
                answer[midr+i] = answer[midr]+i;
            }
        }
        
        return answer;
    }
}