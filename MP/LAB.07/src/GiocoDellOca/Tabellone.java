package GiocoDellOca;
import java.util.Random;

public class Tabellone {
    public final int N;
    private Casella[] caselle;
    private Giocatore[] giocatori;
    
    public Tabellone(int n, Giocatore... giocatori) {
        this.N = n;
        this.giocatori = giocatori;
        caselle = new Casella[N];
        Random r = new Random();
        for (int i=0; i<N; i++) {
            int randInt = r.nextInt(7);
            caselle[i] = switch (randInt) {
                case 1 -> new CasellaPunti();
                case 2 -> new CasellaSpostaGiocatore();
                default -> new CasellaVuota();
            };
        }
    }

    public void muoviGiocatore(Giocatore g) {
        int dadi = g.tiraDadi();
        if (g.getPos()+dadi < N-1) {
            g.setPos(g.getPos()+dadi);
        } else {

        }
    }


}
