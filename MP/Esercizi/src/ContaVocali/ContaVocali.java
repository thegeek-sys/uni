package ContaVocali;

public class ContaVocali {
    private String s;
    private int[] count;
    private final static char[] vowels = new char[] {'a', 'e', 'i', 'o', 'u'};
    public ContaVocali(String s) {
        this.s = s;
        count = new int[5];
    }
    public void stampa() {
        for (int i=0; i<s.length(); i++) {
            for (int j=0; j<vowels.length; j++) {
                if (s.charAt(i) == vowels[j]) {
                    count[j]++;
                }
            }
        }

        System.out.println("a="+count[0]+" e="+count[1]+" i="+count[2]+" o="+count[3]+" u="+count[4]);
    }

    public static void main(String[] args) {
        ContaVocali str = new ContaVocali("le aiuole sono pulite");
        //System.out.println(str.s);
        str.stampa();
    }
}
