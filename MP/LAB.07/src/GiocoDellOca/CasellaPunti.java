package GiocoDellOca;

import java.util.Random;

public class CasellaPunti extends Casella {
    @Override
    public void azione(Giocatore g) {
        Random r = new Random();
        int randPu = r.nextInt(-7, 8);
        g.setPunti(g.getPunti()+randPu);
    }
}
