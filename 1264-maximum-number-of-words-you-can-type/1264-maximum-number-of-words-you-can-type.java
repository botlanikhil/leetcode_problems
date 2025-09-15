class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        String[] s=text.split(" ");
        ArrayList<String> s2=new ArrayList<>(Arrays.asList(s));
        char[] char1=brokenLetters.toCharArray();
        int c=0;
        for(String i:s){
            for (char j:char1){
                if(i.indexOf(j)!=-1 ){
                    s2.remove(i);
                }
            }
        }  
        return s2.size();
    }
}