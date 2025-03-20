package e08_09_23.gestione;

public class Treno {
    private static int id;
    private int numeroVagoni;

    public Treno(int numeroVagoni) {
        this.numeroVagoni = numeroVagoni;
        id++;
    }
}
