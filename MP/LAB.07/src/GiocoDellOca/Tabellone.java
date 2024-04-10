package GiocoDellOca;
import java.util.Random;

public class Tabellone {
    public final static int N = 100;
    private Casella[] caselle;
    private Giocatore[] giocatori;
    
    public Tabellone(int n, Giocatore[] giocatori) {
        //this.N = n;
        this.giocatori = giocatori;
        caselle = new Casella[N];
        Random r = new Random();
        for (int i=0; i<N; i++) {
            int randInt = r.nextInt(5);
            caselle[i] = switch (randInt) {
                case 1 -> new CasellaPunti();
                case 2 -> new CasellaSpostaGiocatore();
                default -> new CasellaVuota();
            };
        }
    }

    // todo: sistemare "effetto gioco dell'oca"
    public void muoviGiocatore(Giocatore g) {
        int dadi = g.tiraDadi();
        boolean tooMuch = false;
        for (int i=0; i<dadi; i++) {
            if (!tooMuch) {
                g.setPos(g.getPos()+1);
            } else {
                g.setPos(g.getPos()-1);
            }
            if (g.getPos() >= N-1) tooMuch=true;
        }
        caselle[g.getPos()].azione(g);
    }

    public Giocatore chekWin(Giocatore[] giocatori) {
        for (Giocatore g : giocatori) {
            if (g.getPos() == N-1) {
                return g;
            }
        }
        return null;
    }

    public String getCell(Giocatore g) {
        return caselle[g.getPos()].getClass().getSimpleName();
    }

    public Giocatore[] getGiocatori() { return giocatori; }
}
