package QUATTRO.concessionaria.model;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Database {
    private ArrayList<Auto> automobili;

    public Database() {
        automobili = new ArrayList<>();
    }

    public void addAuto(Auto auto) {
        automobili.add(auto);
    }

    public List<Auto> getAutomobili() {
        return automobili;
    }

    public void salvaSuFule(File file) throws IOException {
        FileOutputStream fos = new FileOutputStream(file);
        ObjectOutputStream oos = new ObjectOutputStream(fos);

        Auto[] arrayAuto = automobili.toArray(new Auto[automobili.size()]);

        oos.writeObject(arrayAuto);

        oos.close();
        fos.close();

    }

    public void caricaDaFile(File file) throws IOException {
        FileInputStream fis = new FileInputStream(file);
        ObjectInputStream ois = new ObjectInputStream(fis);

        try {
            Auto[] autoCaricate = (Auto[])ois.readObject();

            automobili.clear();

            automobili.addAll(Arrays.asList(autoCaricate));

        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }

        ois.close();
        fis.close();
    }
}
