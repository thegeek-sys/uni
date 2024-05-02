package Treno;

import java.util.ArrayList;

public class VagoneLetto extends Vagone {
    public static final int POSTI = 10;
    private ArrayList<Passeggero> passeggeri = new ArrayList<>();

    public VagoneLetto(String destinazione) {
        super(destinazione, POSTI);
    }

    @Override
    public void occupa(Passeggero passeggero) throws PostiNonDisponibiliException, PasseggeroNonAmmessoException {
        if (postiDisponibili == 0) {
            throw new PostiNonDisponibiliException("Posti per "+getClass().getSimpleName()+" esauriti");
        }
        if (!(passeggero.getClass().getSimpleName().equals("PasseggeroAssonnato"))) {
            throw new PasseggeroNonAmmessoException("Passeggero di tipo "+passeggero.getClass().getSimpleName()+" non ammesso su questo vagone");
        }
        postiDisponibili -= 1;
        passeggeri.add(passeggero);
        System.out.println("Passeggero "+passeggero.getNome()+" registrato");
    }

    public String getPasseggeri() {
        StringBuilder p = new StringBuilder();
        for (int i=0; i<passeggeri.size(); i++) {
            p.append(passeggeri.get(i).getNome());
            if (i!=passeggeri.size()-1) {
                p.append(", ");
            }
        }

        return p.toString();
    }
}


