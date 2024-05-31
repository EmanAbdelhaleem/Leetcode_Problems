class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans = INT_MIN;
        int temp = 0; int mx = INT_MIN;
        for(int i = 0; i < nums.size(); i++){
            if(temp + nums[i] >=1){
                temp+=nums[i];
                ans = max(ans,temp);
            }else temp = 0;
            mx = max(mx,nums[i]);
        }
        if(mx<1) return mx;
        return ans;
    }
};