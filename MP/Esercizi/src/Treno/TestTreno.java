package Treno;

public class TestTreno {
    public static void main(String[] args) throws DestinazioneDiversaException, LocomotiveMultipleException, PasseggeroNonAmmessoException, PostiNonDisponibiliException {
        Treno treno = new Treno("Milano");
        VagoneLetto vagone1 = new VagoneLetto("Milano");
        treno.aggiungiVagone(vagone1);
        vagone1.occupa(new PasseggeroAssonnato());
        vagone1.occupa(new PasseggeroAssonnato());
        vagone1.occupa(new PasseggeroAssonnato());
        vagone1.occupa(new PasseggeroAssonnato());
        vagone1.occupa(new PasseggeroAssonnato());
        vagone1.occupa(new PasseggeroAssonnato());
        vagone1.getPasseggeri();
        VagonePasseggeri vagone2 = new VagonePasseggeri("Milano");
        vagone2.getPasseggeri();
        System.out.println(treno);

    }
}
