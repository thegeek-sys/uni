package Cerchio;

public class Cerchio {
    private final double raggio;
    public Cerchio(double raggio) {
        this.raggio = raggio;
    }
    public double getArea() {
        return Math.PI*Math.pow(raggio, 2);
    }
    public double getCirconferenza() {
        return 2*Math.PI*raggio;
    }

    public static void main(String[] args) {
        Cerchio c1 = new Cerchio(1);
        Cerchio c2 = new Cerchio(5);

        System.out.println("Circonferenza c1: "+c1.getCirconferenza());
        System.out.println("Area c2: "+c2.getArea());

    }
}
