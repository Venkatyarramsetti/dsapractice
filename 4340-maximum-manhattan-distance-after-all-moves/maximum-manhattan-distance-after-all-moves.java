class Solution {
    public int maxDistance(String moves) {
        int x=0;
        int y=0;
        int c=0;
        for (char i:moves.toCharArray()){
            if (i == 'U'){ y++;}
            else if (i=='D'){ y--;}
            else if (i=='L') {x--;}
            else if (i=='R') {x++;}
            else {c++;}
        }
        return Math.abs(x)+Math.abs(y)+c;
    }
}