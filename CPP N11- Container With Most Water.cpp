class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0, j = height.size() - 1, max = 0;
        int area;
        while (i < j) {
            if (height[i] > height[j]) {
                area = height[j] * (j - i);
                j--;
            }
            else {
                area = height[i] * (j - i);
                i++;
            }
            if (area > max) {
                max = area;
            }
        }
        return max;
    }
};