package e13_07_23.memoria;

public class Main {
    public static void main(String[] args) {
        String s;
        String t;
        int k;
        Integer j;
        Animale a = new Gatto(0);
        Gatto b = new Gatto(1);
        t = ((Gatto)a).toString();
        s=b.toString();
        boolean e = s.equals(t);
        System.out.println("ciao");
    }
}
