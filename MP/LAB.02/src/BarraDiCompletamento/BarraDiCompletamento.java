package BarraDiCompletamento;

public class BarraDiCompletamento {
    private double perc;
    public BarraDiCompletamento(double perc) {
        this.perc = perc;
    }
    public BarraDiCompletamento() {
        perc = 0;
    }
    public void incrementa(double perc) {
        this.perc += perc;
    }

    public String toString() {
        return Math.round(perc)+"%";
    }

    public static void main(String[] args) {
        BarraDiCompletamento bar = new BarraDiCompletamento();
        bar.incrementa(10);
        bar.incrementa(25);
        System.out.println(bar.toString());
    }
}
