package e08_09_23.gestione;

import e13_06_23.gestione.Volume;

public class Stazione {
    private String nome;
    private String indirizzo;

    public Stazione(String nome, String indirizzo) {
        this.nome = nome;
        this.indirizzo = indirizzo;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || this.getClass() != o.getClass()) return false;
        Stazione s = (Stazione) o;
        return s.nome.equals(nome) && s.indirizzo.equals(indirizzo);
    }
}
