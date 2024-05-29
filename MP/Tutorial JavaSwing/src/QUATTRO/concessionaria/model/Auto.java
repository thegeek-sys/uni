package QUATTRO.concessionaria.model;

import java.io.Serializable;

public class Auto implements Serializable {
    private static int contatore = 0;
    private int id;

    private String marca;
    private String modello;
    private boolean vendita;
    private String targa;
    private Cambio cambio;
    private Bagagliaio bagagliaio;
    private String alimentazione;
    private int immatricolazione;
    private int cilindrata;
    private String colore;

    public Auto(String marca, String modello, boolean vendita,
                String targa, Cambio cambio, Bagagliaio bagagliaio,
                String alimentazione, int immatricolazione, int cilindrata, String colore) {
        id = contatore++;
        this.marca = marca;
        this.modello = modello;
        this.vendita = vendita;
        this.targa = targa;
        this.cambio = cambio;
        this.bagagliaio = bagagliaio;
        this.alimentazione = alimentazione;
        this.immatricolazione = immatricolazione;
        this.cilindrata = cilindrata;
        this.colore = colore;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModello() {
        return modello;
    }

    public void setModello(String modello) {
        this.modello = modello;
    }

    public boolean isVendita() {
        return vendita;
    }

    public void setVendita(boolean vendita) {
        this.vendita = vendita;
    }

    public String getTarga() {
        return targa;
    }

    public void setTarga(String targa) {
        this.targa = targa;
    }

    public Cambio getCambio() {
        return cambio;
    }

    public void setCambio(Cambio cambio) {
        this.cambio = cambio;
    }

    public Bagagliaio getBagagliaio() {
        return bagagliaio;
    }

    public void setBagagliaio(Bagagliaio bagagliaio) {
        this.bagagliaio = bagagliaio;
    }

    public String getAlimentazione() {
        return alimentazione;
    }

    public void setAlimentazione(String alimentazione) {
        this.alimentazione = alimentazione;
    }

    public int getImmatricolazione() {
        return immatricolazione;
    }

    public void setImmatricolazione(int immatricolazione) {
        this.immatricolazione = immatricolazione;
    }

    public int getCilindrata() {
        return cilindrata;
    }

    public void setCilindrata(int cilindrata) {
        this.cilindrata = cilindrata;
    }

    public String getColore() {
        return colore;
    }

    public void setColore(String colore) {
        this.colore = colore;
    }
}
