package QUATTRO.concessionaria.model;

public enum Bagagliaio {
    PICCOLO("piccolo"), MEDIO("medio"), GRANDE("grande");

    private String bagagliaio;

    Bagagliaio(String bagagliaio) {
        this.bagagliaio = bagagliaio;
    }

    public String getBagagliaio() {
        return bagagliaio;
    }
}
