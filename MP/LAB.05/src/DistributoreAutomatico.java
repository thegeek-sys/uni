import java.util.Random

public class DistributoreAutomatico {
    private double saldo;
    private Prodotto[] prodotti;
    private final int N;

    public DistributoreAutomatico(int N) {
        this.N = N;
        prodotti = new Prodotto[N];
    }

    public void carica() {
        Random r = new Random();
        for (int i=0; i<N; i++) {
            switch (r.nextInt(3)) {
                case 0: prodotti[i] = new GommeDaMasticare(); break;
                case 1: prodotti[i] = new BottigliaDAcqua(); break;
                case 2: prodotti[i] = new BarraDiCioccolato(); break;
            }
        }
    }

    public void getProdotto(int id) {
        for (int i=0; i<N; i++) {
            if (prodotti[i] != null && prodotti[i].ID == id && prodotti[i].PREZZO <= saldo) {
                prodotti[i] = null;
                saldo -= prodotti[i].PREZZO;
                System.out.println(prodotti[i]);
                break;
            }
        }
    }

    public void inserisciImporto(double importo) {
        saldo += importo;
        System.out.println("Saldo: "+saldo+"€");
    }

    public double getSaldo() { return saldo; }
    public double getResto() {
        double resto = saldo;
        saldo = 0;
        return resto;
    }

    public static void main(String[] args) {
        DistributoreAutomatico d = new DistributoreAutomatico(5);
        d.inserisciImporto(5);
        d.getProdotto(2);
    }
}
