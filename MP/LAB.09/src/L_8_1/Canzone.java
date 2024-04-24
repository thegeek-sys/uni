package L_8_1;

import java.util.Comparator;

public class Canzone implements Comparable<Canzone> {
    private String nome;
    private String autore;

    public Canzone(String nome, String autore) {
        this.nome = nome;
        this.autore = autore;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null) return false;
        if (getClass() != o.getClass()) return false;
        Canzone c = (Canzone)o;
        return (c.autore.equals(autore) && c.nome.equals(nome));
    }
    @Override
    public int hashCode() {
        if (nome != null && autore != null) {
            int prime = 31;
            int result = 17;

            result = result*prime + nome.hashCode();
            result = result*prime + autore.hashCode();

            return result;
        }
        return 0;
    }
    @Override
    public String toString() {
        return nome + " - " + autore;
    }
    @Override
    public int compareTo(Canzone c) {
        int n = nome.compareTo(c.nome);
        return n==0 ? autore.compareTo(c.autore) : n;
    }
}
