package gestione;

public class Ex2_CartaPokemon extends Ex2_AbstractCartaPokemon implements Comparable<Ex2_CartaPokemon> {
    private final TipologiaPokemon tipologiaPokemon;
    private final TipologiaCarta tipologiaCarta;
    private final String nome;
    private final int hp;

    public Ex2_CartaPokemon(String nome, TipologiaPokemon tipologiaPokemon, TipologiaCarta tipologiaCarta, int hp) {
        this.nome = nome;
        this.tipologiaPokemon = tipologiaPokemon;
        this.tipologiaCarta = tipologiaCarta;
        this.hp = hp;
    }

    @Override
    public String toString() {
        return "Nome: "+nome+", tipologia Pokemon: "+tipologiaPokemon+", tipologia carta: "+tipologiaCarta+", HP: "+hp;
    }

    @Override
    public void stampa() {
        System.out.println(this);
    }

    public String getNome() {
        return nome;
    }

    @Override
    public int compareTo(Ex2_CartaPokemon o) {
        return Integer.compare(hp, o.hp);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Ex2_CartaPokemon carta = (Ex2_CartaPokemon) o;
        return hp == carta.hp && tipologiaPokemon == carta.tipologiaPokemon && tipologiaCarta == carta.tipologiaCarta && nome.equals(carta.nome);
    }

    @Override
    public int hashCode() {
        int result = 37;
        result *= nome.hashCode();
        result *= tipologiaPokemon.hashCode();
        result *= tipologiaCarta.hashCode();
        result *= hp;
        return result;
    }

    public enum TipologiaPokemon {
        NORMALE, FUOCO, ACQUA, ERBA, ELETTRO, GHIACCIO, LOTTA, VELENO, TERRA, VOLANTE, PSICO, COLEOTTERO, ROCCIA, SPETTRO, DRAGO, BUIO, ACCIAIO, FOLLETTO;
    }

    public enum TipologiaCarta {
        NORMALE, SHINING, REVERSE, V, V_MAX, G, G_MAX, FULL_ART;
    }
}
