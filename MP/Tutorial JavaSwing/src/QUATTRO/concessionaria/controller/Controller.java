package QUATTRO.concessionaria.controller;

import QUATTRO.concessionaria.model.Auto;
import QUATTRO.concessionaria.model.Bagagliaio;
import QUATTRO.concessionaria.model.Cambio;
import QUATTRO.concessionaria.model.Database;

import java.io.File;
import java.io.IOException;
import java.util.List;

public class Controller {
    private Database database = new Database();

    public void addAuto(String marca, String modello, boolean vendita,
                        String targa, String cambioString, int bagagliaioInt,
                        String alimentazione, int immatricolazione,
                        int cilindrata, String colore) {

        Cambio cambio = Cambio.valueOf(cambioString.toUpperCase());
        Bagagliaio bagagliaio = switch (bagagliaioInt) {
            case 0 -> Bagagliaio.PICCOLO;
            case 1 -> Bagagliaio.MEDIO;
            case 2 -> Bagagliaio.GRANDE;
            default -> throw new IllegalStateException("Unexpected value: " + bagagliaioInt);

        };

        Auto auto = new Auto(marca, modello,  vendita, targa, cambio, bagagliaio, alimentazione, immatricolazione, cilindrata, colore);

        database.addAuto(auto);
    }

    public List<Auto> getAutomobili() {
        return database.getAutomobili();
    }

    public void salvaSuFile(File file) throws IOException {
        database.salvaSuFule(file);
    }

    public void caricaDaFile(File file) throws IOException {
        database.caricaDaFile(file);
    }
}
