class Solution {
    public int longestValidParentheses(String s) {
        ArrayList<Integer> open_p = new ArrayList<Integer>();
        ArrayList<Integer> close_p = new ArrayList<Integer>();
        for (int i = 0; i < s.length(); i++) {
            if (s.substring(i, i + 1).equals("(")) {
                open_p.add(i);
            }
            else if (s.substring(i, i + 1).equals(")")) {
                close_p.add(i);
            }
        }
        ArrayList<Integer> placement = new ArrayList<Integer>();
        for (int j = 0; j < close_p.size(); j++) {
            if (open_p.size() == 0) {
                continue;
            }
            else if (close_p.size() == 0) {
                continue;
            } 
            for (int k = open_p.size() - 1; k >= 0; k--) {
                if (open_p.size() == 0) {
                    continue;
                }
                else if (close_p.size() == 0) {
                    continue;
                }
                if (open_p.get(k) < close_p.get(j)) {
                    placement.add(close_p.get(j));
                    placement.add(open_p.get(k));
                    close_p.remove(j);
                    open_p.remove(k);
                    j--;
                    j = Math.max(j, 0);
                    k = open_p.size();
                }
            }
        }
        if (placement.size() == 0) {
            return 0;
        }
        Collections.sort(placement);
        int max_length = 0;
        int current = 1;
        for (int n = 0; n < placement.size() - 1; n++) {
            int x = placement.get(n + 1);
            x--;
            int y = placement.get(n);
            if (x == y) {
                current++;
            }
            else {
                max_length = Math.max(max_length, current);
                current = 1;
            }
        }
        if (max_length % 2 == 1) {
            max_length--;
            return max_length;
        }
        else {
            return Math.max(max_length, current);
        }
    }
}