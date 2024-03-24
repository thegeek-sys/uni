package L_3_3;

public class L_3_3 {
    public static void stampaVerticale(String s1, String s2, String s3) {
        int m = Math.max(s1.length(), s2.length());
        int max = Math.max(m, s3.length());

        for (int i=0; i<max; i++) {
            char c1 = i<s1.length() ? s1.charAt(i) : ' ';
            char c2 = i<s2.length() ? s2.charAt(i) : ' ';
            char c3 = i<s3.length() ? s3.charAt(i) : ' ';
            System.out.println(""+c1+c2+c3);
        }
    }

    public static void main(String[] args) {
        stampaVerticale("ciao", "buondì", "hello");
    }
}
