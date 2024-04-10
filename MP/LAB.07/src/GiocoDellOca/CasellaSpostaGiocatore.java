package GiocoDellOca;
import java.util.Random;

public class CasellaSpostaGiocatore extends Casella{
    @Override
    public void azione(Giocatore g) {
        Random r = new Random();
        int randSpo;
        do {
            randSpo = r.nextInt(-7, 8);
        } while (g.getPos()+randSpo>=Tabellone.N);
        g.setPos(g.getPos()-randSpo);
    }
}
