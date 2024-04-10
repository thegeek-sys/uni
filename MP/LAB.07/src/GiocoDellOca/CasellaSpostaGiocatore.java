package GiocoDellOca;
import java.util.Random;

public class CasellaSpostaGiocatore extends Casella{
    @Override
    public void azione(Giocatore g) {
        Random r = new Random();
        int randSpo = r.nextInt(-7, 8);
        g.setPos(g.getPos()+randSpo);
    }
}
