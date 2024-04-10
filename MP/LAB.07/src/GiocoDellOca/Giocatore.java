package GiocoDellOca;
import java.util.Random;

public class Giocatore {
    private int punti;
    private int pos;
    private final String nome;

    public Giocatore(String nome) {
        this.nome = nome;
        pos = 0;
        punti = 0;
    }

    public int tiraDadi() {
        Random r = new Random();
        return r.nextInt(2,13);
    }

    public int getPos() { return pos; }
    public int getPunti() { return punti; }
    public String getNome() { return nome; }
    public void setPunti(int p) { punti=p; }
    public void setPos(int p) { pos=p; }
}
