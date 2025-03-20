package e08_09_23.gestione;

public class TrenoMerci extends Treno {
    private int quintaliTrasportabili;

    public TrenoMerci(int numeroVagoni, int quintaliTrasportabili) {
        super(numeroVagoni);
        this.quintaliTrasportabili = quintaliTrasportabili;
    }
}
