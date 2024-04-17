package dinsey_vs_marvel;

public class Paperino extends PersonaggioDisney implements DoppiaVita {
    public static final String NOME_PAPERINO = "Paperino";
    private static Paperino instance;

    private Paperino() {
        this(NOME_PAPERINO);
    }
    private Paperino(String nome) {
        super(nome);
    }

    public static Paperino getInstance() {
        if (instance == null) {
            instance = new Paperino();
        }
        return instance;
    }

    @Override
    public Personaggio assumiIdentitaSegreta() {
        return Paperinik.getInstance();
    }

    @Override
    public Personaggio assumiIdentitaPubblica() {
        return Paperino.getInstance();
    }

    @Override
    public void saluta() {

    }

    private class Paperinik extends Paperino implements SuperEroe {
        public static final String NOME_PAPERINIK = "Paperinik";
        private static Paperinik instance;

        private Paperinik() {
            super(NOME_PAPERINIK);
        }

        public static Paperinik getInstance() {
            if (instance == null) {
                instance = Paperino.getInstance().new Paperinik();
            }
            return instance;
        }

        @Override
        public void attacca() {

        }
    }
}
