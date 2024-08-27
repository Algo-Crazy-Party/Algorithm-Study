#include <vector>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int maxIdx = nums.size()-1;
        vector<pair<int,int>> v;
        for (int i=0; i<=maxIdx; i++) {
            v.push_back({nums[i], i});
        }
        sort(v.begin(), v.end());

        int left = 0;
        int right = maxIdx;
        int sum = 0;

        while (left < right) {
            sum = v[left].first + v[right].first;
            // 2 7 11 15
            if (sum == target) {
                break;
            } else if (sum > target) {
                right--;
            } else {
                left++;
            }
        }



        vector<int> ans;
        ans.push_back(v[left].second);
        ans.push_back(v[right].second);
        return ans;
    }
};