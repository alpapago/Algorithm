class Solution {
public:
    int maxArea(vector<int>& height) {
        int answer = 0;
        int s = 0;
        int e = height.size()-1;
        
        while(s<e){
            int area;
            int h = min(height[s], height[e]);
            int w = e-s;
            area = h*w;
            
            if(area > answer){
                answer = area;
            }
            
            if(height[s] <= height[e]){
                s++;
            }
            else{
                e--;
            }
        }
        return answer;
    }
};