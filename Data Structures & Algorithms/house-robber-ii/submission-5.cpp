class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        return max(rob_linear(nums, 0, n - 1), rob_linear(nums, 1, n));

    }
private:
    int rob_linear(const vector<int>& nums, int start, int end) {
        int n = end - start;
        vector<int> dp(n + 1);
        dp[0] = nums[start];
        if (n > 1) dp[1] = max(nums[start], nums[start + 1]);
        for (int i = 2; i < n; ++i) {
            dp[i] = max(dp[i - 1], nums[start + i] + dp[i - 2]);
        }
        return (dp[n - 1]);
    }
};