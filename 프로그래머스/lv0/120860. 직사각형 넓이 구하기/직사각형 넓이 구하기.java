class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        int ver =0;
        int hor =0;
        
        for(int i=0;i<3;i++){
            if(dots[i][0]==dots[i+1][0]){
                hor = Math.abs(dots[i][1]-dots[i+1][1]);
            }else{
                ver = Math.abs(dots[i][0]-dots[i+1][0]);
            }
        }
        answer = ver*hor;

        return answer;
    }
}