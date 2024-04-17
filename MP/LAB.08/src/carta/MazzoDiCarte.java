package carta;

import java.util.Iterator;

public class MazzoDiCarte implements Iterable<Carta> {
    private Carta[] mazzo = new Carta[52];
    private int cursore;

    public MazzoDiCarte() {
        int k=0;
        for (int i=0; i<Semi.values().length; i++) {
            for(int j=0; j<Valori.values().length; j++) {
                mazzo[k++] = new Carta(Semi.values()[i], Valori.values()[j]);
            }
        }
    }


    @Override
    public Iterator<Carta> iterator() {
        return new Iteratore();
    }

    private class Iteratore implements Iterator<Carta> {
        private int cursoreIt;

        @Override
        public boolean hasNext() {
            return cursoreIt<mazzo.length;
        }

        @Override
        public Carta next() {
            return mazzo[cursoreIt++];
        }
    }


}
