package carta;

import java.util.Objects;

public class Carta {
    private final Semi seme;
    private final Valori valore;

    public Carta(Semi seme, Valori valore) {
        this.seme = seme;
        this.valore = valore;
    }

    public String toString() {
        return valore.getValore()+" di "+seme.getSeme();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || !(this.getClass().equals(o.getClass()))) return false;
        Carta carta = (Carta)o;
        return seme.equals(carta.seme) && valore.equals(carta.valore);
    }

    @Override
    public int hashCode() {
        return 37*seme.hashCode()+valore.hashCode();
    }
}
