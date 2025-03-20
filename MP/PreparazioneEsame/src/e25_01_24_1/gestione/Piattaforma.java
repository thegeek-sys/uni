package e25_01_24_1.gestione;

import java.util.Objects;

public class Piattaforma {
    private String nome;
    private int annoUscita;
    private String produttore;
    private boolean mobile;
    private int bit;

    private Piattaforma(Builder builder) {
        nome = builder.nome;
        annoUscita = builder.annoUscita;
        produttore = builder.produttore;
        mobile = builder.mobile;
        bit = builder.bit;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Piattaforma that)) return false;
        return annoUscita == that.annoUscita && mobile == that.mobile && bit == that.bit && Objects.equals(nome, that.nome) && Objects.equals(produttore, that.produttore);
    }

    @Override
    public int hashCode() {
        return Objects.hash(nome, annoUscita, produttore, mobile, bit);
    }

    public String getNome() {
        return nome;
    }

    public int getAnnoUscita() {
        return annoUscita;
    }

    public String getProduttore() {
        return produttore;
    }

    public boolean isMobile() {
        return mobile;
    }

    public int getBit() {
        return bit;
    }

    public static class Builder {
        private String nome;
        private int annoUscita;
        private String produttore;
        private boolean mobile;
        private int bit;

        public Builder(String nome, int annoUscita, String produttore) {
            this.nome = nome;
            this.annoUscita = annoUscita;
            this.produttore = produttore;
        }

        public Builder setMobile(boolean mobile) {
            this.mobile = mobile;
            return this;
        }

        public Builder setBit(int bit) {
            this.bit = bit;
            return this;
        }

        public Piattaforma build() {
            return new Piattaforma(this);
        }

    }
}
