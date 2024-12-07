class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int,int>> nums_;
        vector<int> ans;
        int n = nums.size();
        for(int i=0; i < n; i++){
            nums_.push_back(make_pair(nums[i],i));
        }
        
        sort(nums_.begin(), nums_.end());
        int s = 0;
        int e = n-1;
        while(s<e){
            int tmp = nums_[s].first + nums_[e].first;
            if(tmp == target){
                if(nums_[s].second < nums_[e].second){
                    ans.push_back(nums_[s].second);
                    ans.push_back(nums_[e].second);
                }
                else{
                    ans.push_back(nums_[e].second);
                    ans.push_back(nums_[s].second);
                }
                break;
            }
            else if(tmp > target){
                e--;
            }
            else{
                s++;
            }
        }
        return ans;
    }
};