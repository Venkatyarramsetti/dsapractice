class Solution {
    public String rearrangeString(String s, char x, char y) {
        String xs = "";
        String ys = "";
        String re = "";
        for(int j=0;j<s.length();j++){
            char i = s.charAt(j);
            if(i == x) xs +=i;
            else if(i == y) ys += i;
            else re += i;
        }
        return ys+re+xs;
    }
}