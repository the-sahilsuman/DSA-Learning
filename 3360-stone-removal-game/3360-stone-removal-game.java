class Solution {
    public boolean canAliceWin(int n) {
        String turn = "Bob";
        int stones = 10;

        while (n >= stones) {
            n -= stones;
            turn = turn.equals("Bob") ? "Alice" : "Bob";
            stones--;
        }

        return turn.equals("Alice");
    }
}