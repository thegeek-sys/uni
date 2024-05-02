package Treno;

public class Locomotiva extends Vagone {
    public static final int POSTI = 0;

    public Locomotiva(String destinazione) {
        super(destinazione, POSTI);
    }

    @Override
    public void occupa(Passeggero passeggero) throws PostiNonDisponibiliException {
        throw new PostiNonDisponibiliException("Posti per "+getClass().getSimpleName()+" esauriti");
    }
}
