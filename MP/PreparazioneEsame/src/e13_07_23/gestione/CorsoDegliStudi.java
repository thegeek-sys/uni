package e13_07_23.gestione;

import java.util.HashMap;

public class CorsoDegliStudi {
    private String nomeCorso;
    private HashMap<Insegnamento, Integer> mappaInsegnamento;

    public CorsoDegliStudi(String nomeCorso) {
        this.nomeCorso = nomeCorso;
        mappaInsegnamento = new HashMap<>();
    }

    public void addInsegnamento(Insegnamento insegnamento, Integer cfu) {
        mappaInsegnamento.put(insegnamento, cfu);
    }
}
