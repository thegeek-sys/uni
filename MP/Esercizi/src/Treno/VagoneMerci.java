package Treno;

public class VagoneMerci extends Vagone {
    public static final int POSTI = 0;

    public VagoneMerci(String destinazione) {
        super(destinazione, POSTI);
    }

    @Override
    public void occupa(Passeggero passeggero) throws PostiNonDisponibiliException {
        throw new PostiNonDisponibiliException("Posti per "+getClass().getSimpleName()+" esauriti");
    }
}
