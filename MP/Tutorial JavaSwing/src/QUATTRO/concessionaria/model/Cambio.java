package QUATTRO.concessionaria.model;

public enum Cambio {
    MANUALE("manuale"), AUTOMATICO("automatico");
    private String cambio;

    Cambio(String cambio) {
        this.cambio = cambio;
    }

    public String getCambio() {
        return cambio;
    }
}
