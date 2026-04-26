using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int longest = 0;
        int l = 0;
        unordered_set<char> window;
        for (int r = 0; r < s.length(); ++r) {
            while (window.count(s[r])) {
                window.erase(s[l]);
                l+=1;
            }
            window.insert(s[r]);
            longest = max(longest, r-l+1);
        }
        return longest;
    }
};
