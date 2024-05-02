package Treno;

import java.util.ArrayList;

public class Treno {
    private ArrayList<Vagone> treno = new ArrayList<Vagone>();

    public Treno(String destinazione) {
        treno.add(new Locomotiva(destinazione));
    }
    public Treno(ArrayList<Vagone> treno) {
        this.treno = treno;
    }

    public void aggiungiVagone(Vagone vagone) throws DestinazioneDiversaException, LocomotiveMultipleException {
        if (!(vagone.getDestinazione().equals(treno.getFirst().getDestinazione()))) {
            throw new DestinazioneDiversaException("Vagone: "+vagone.getDestinazione()+", treno: "+treno.getFirst().getDestinazione());
        }
        if (vagone.getClass() == treno.getFirst().getClass()) {
            throw new LocomotiveMultipleException();
        }
        treno.add(vagone);
    }

    public Treno dividiTreno(int k, Locomotiva locomotiva) {
        ArrayList<Vagone> newTreno = new ArrayList<Vagone>();
        newTreno.add(locomotiva);
        for(int i=k; i<treno.size(); i++) {
            newTreno.add(treno.get(i));
        }
        treno.removeAll(newTreno);
        return new Treno(newTreno);
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        for (Vagone vagone : treno) {
            s.append(vagone.getClass().getSimpleName());
            s.append(treno.indexOf(vagone)!=treno.size()-1 ? "--" : "");
        }
        return s.toString();
    }
}
