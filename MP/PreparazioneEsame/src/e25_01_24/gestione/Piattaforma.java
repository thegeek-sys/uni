package e25_01_24.gestione;

public class Piattaforma {
    private String nome;
    private int anno;
    private String produttore;
    private boolean mobile;
    private int architettura;

    public Piattaforma(PiattaformaBuilder builder) {
        this.nome = builder.nome;
        this.anno = builder.anno;
        this.produttore = builder.produttore;
        this.mobile = builder.mobile;
        this.architettura = builder.architettura;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Piattaforma p = (Piattaforma)o;
        return nome.equals(p.nome) && anno == p.anno && produttore.equals(p.produttore) && mobile == p.mobile && architettura == p.architettura;
    }

    public int getArchitettura() {
        return architettura;
    }

    public static class PiattaformaBuilder {
        private String nome;
        private int anno;
        private String produttore;
        // opt
        private boolean mobile;
        private int architettura;

        public PiattaformaBuilder(String nome, int anno, String produttore, boolean mobile, int architettura) {
            this.nome = nome;
            this.anno = anno;
            this.produttore = produttore;
        }

        public PiattaformaBuilder setMobile(boolean mobile) {
            this.mobile = mobile;
            return this;
        }

        public PiattaformaBuilder setArchitettura(int architettura) {
            this.architettura = architettura;
            return this;
        }

        public Piattaforma build() {
            return new Piattaforma(this);
        }

    }



}
