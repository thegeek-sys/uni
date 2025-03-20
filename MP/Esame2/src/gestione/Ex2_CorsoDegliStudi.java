package gestione;

import java.util.HashMap;

public class Ex2_CorsoDegliStudi {
    private String nomeCorso;
    private HashMap<Ex2_Insegnamento, Integer> mappaInsegnamentoCFU;

    public Ex2_CorsoDegliStudi(String nomeCorso) {
        this.nomeCorso = nomeCorso;
        mappaInsegnamentoCFU = new HashMap<>();
    }

    public void addInsegnamento(Ex2_Insegnamento insegnamento, int CFU) {
        mappaInsegnamentoCFU.put(insegnamento, CFU);
    }

    public void removeInsegnamento(Ex2_Insegnamento insegnamento) {
        mappaInsegnamentoCFU.remove(insegnamento);
    }

    public String getNomeCorso() {
        return nomeCorso;
    }

    public HashMap<Ex2_Insegnamento, Integer> getMappaInsegnamentoCFU() {
        return mappaInsegnamentoCFU;
    }
}
