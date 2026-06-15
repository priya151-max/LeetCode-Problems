class Solution {
    public boolean checkIfCanBreak(String s1, String s2) {
        char chS1 [] = s1.toCharArray();
        char chS2 [] = s2.toCharArray();
        Arrays.sort(chS1);
        Arrays.sort(chS2);
        boolean flagChS1 = true;
        for (int i=0; i<chS1.length; i++) {
            if (chS2[i] < chS1[i]) {
                flagChS1 = false;
                break;
            }
        }
        boolean flagChS2 = true;
        for (int i=0; i<chS2.length; i++) {
            if (chS1[i] < chS2[i]) {
                flagChS2 = false;
                break;
            }
        }
        return flagChS1 || flagChS2;
    }
}