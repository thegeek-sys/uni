package e25_01_24.memoria;

public class Main {
    public static void main(String[] args) {
        String s;
        String t;
        long k;
        Integer j;
        Persona a=new Persona(5);
        EssereVivente b = new Persona(2);
        t = ((Persona)b).toString();
        s=a.toString();
        boolean e=s.equals(t);
        k = s.length();
        System.out.println(EssereVivente.numeroEsseriViventi);
    }
}
