package L_2_5;

public class TestRettangolo {
    public static void main(String[] args) {
        Rettangolo rect = new Rettangolo(0,0,20,10);
        rect.trasla(10,5);
        System.out.println(Colore.BIANCO);
        System.out.println(rect.toString());
        System.out.println(rect.getColore());
        rect.setColore(132,0,37);
        System.out.println(rect.getColore());

    }
}
