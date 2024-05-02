package Treno;

import java.util.ArrayList;

public class VagonePasseggeri extends Vagone{
    public static final int POSTI = 50;
    private ArrayList<Passeggero> passeggeri = new ArrayList<>();

    public VagonePasseggeri(String destinazione) {
        super(destinazione, POSTI);
    }

    @Override
    public void occupa(Passeggero passeggero) throws PostiNonDisponibiliException {
        if (postiDisponibili == 0) {
            throw new PostiNonDisponibiliException("Posti per "+getClass().getSimpleName()+" esauriti");
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
