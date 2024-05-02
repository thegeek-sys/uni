package PECS;

import java.util.Arrays;
import java.util.List;

public class Main {


    public static <T> void copy(T[] src, T[] dst) {
        dst[0] = src[0];
        // src producer
        // dst consumer (consuma ciò che viene prodotto)
    }

    public static <T> void copyListNOPECS(List<T> src, List<T> dst) {
        for (T o : src)
            dst.add(o);
    }

    public static <T> void copyListPECS(List<? extends T> src, List<? super T> dst) {
        for (T o : src)
            dst.add(o);
    }



    public static void main(String[] args) {

        Mela[] mele = new Mela[] {new Mela(), new Mela()};
        Pera[] pere = new Pera[] {new Pera(), new Pera()};

        copy(mele, pere);
        // polimorfismo agisce sugli array in java, sia l'array di mela che l'array di pera sono array di pera
        // non ho errori sull'ide perché l'errore di consistenza sul tipo vengono fatti solamente dal compilatore
        // il compilatore mi restituisce ArrayStoreException

        // il PECS in questo caso non ci può risolvere questo problema in quanto è applicabile solo alle Collection
        // utilizzo le Collection poiché i tipi delle Collection sono generici
        List<Mela> lmele = Arrays.asList(mele);
        List<Pera> lpere = Arrays.asList(pere);
        copyListNOPECS(lmele, lpere); // NON rispetta il vincolo di essere dello stesso tipo T
        copyListNOPECS(lmele, lmele); // rispetta il vincolo di essere dello stesso tipo T

        List<Frutto> lfrutti = Arrays.asList(new Frutto[]{new Pera(), new Mela()});
        copyListNOPECS(lmele, lfrutti); // List<Mela> non può essere convertito a List<Frutto>, non vale il polimorfismo

        copyListPECS(lmele, lfrutti); // il tipo della lista di destinazione può essere Mela, Frutto o Object
    }
}
