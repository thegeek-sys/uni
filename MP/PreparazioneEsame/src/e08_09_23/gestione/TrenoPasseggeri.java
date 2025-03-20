package e08_09_23.gestione;

public class TrenoPasseggeri extends Treno{
    private int numeroPasseggeri;

    public TrenoPasseggeri(int numeroVagoni, int numeroPasseggeri) {
        super(numeroVagoni);
        this.numeroPasseggeri = numeroPasseggeri;
    }
}
