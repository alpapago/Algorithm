import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0; //시간
        int sum =0;//weight비교하려고
        Queue<Integer> bridge = new LinkedList<>();

        for(int i=0;i<truck_weights.length;i++){
            int truck = truck_weights[i];//트럭한대씩 뽑아
            while(true){
                if(bridge.isEmpty()){
                    bridge.add(truck);
                    answer++;
                    sum+=truck;
                    break;
                }else if(bridge.size()==bridge_length){
                    sum -=bridge.poll();
                }else{
                    if(sum+truck>weight){
                        bridge.add(0);
                        answer++;
                    }else{
                        bridge.add(truck);
                        sum+=truck;
                        answer++;
                        break;
                    }
                }
            }

        }
        return answer+bridge_length;
    }
}