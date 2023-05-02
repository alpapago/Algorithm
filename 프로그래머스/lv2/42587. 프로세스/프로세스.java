import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        int l = location;
        int n = priorities.length-1;//최댓값 하나씩 끌어 내림
        
        Queue<Integer> q = new LinkedList<>();
        
        for(int i : priorities){ //q에집어넣음
            q.add(i);
        }

        Arrays.sort(priorities); //최댓값을위해  배열 sorting

        while(true){
            if(priorities[n-answer] == q.peek()){
                q.poll();//실행시킴
                l--;//q한칸씩 줄임
                answer++;//실행 횟수 하나 늘림.
                if(l<0){
                    break; //원하는 바를 이루면 종료
                }
            }else{//우선순위 가장 높은 녀석이 아니라면
                q.add(q.poll());
                l--; //poll했으니까 한칸씩줄여주고
                if(l<0){
                    l = q.size()-1;//아직 우선순위 안됬으면, q에서 인덱스 조정.
                }
            }
        }

        return answer;
    }
}