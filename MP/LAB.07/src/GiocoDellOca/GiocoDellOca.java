package GiocoDellOca;

import java.util.Scanner;

public class GiocoDellOca {
    public static void main(String[] args) {
        Giocatore[] players = new Giocatore[2];
        players[0] = new Giocatore("Flavio");
        players[1] = new Giocatore("Vlad");

        Tabellone t = new Tabellone(100, players);

        while (t.chekWin(players) == null) {
            for (Giocatore player : players) {
                t.muoviGiocatore(player);
                System.out.println(player.getNome());
                System.out.println("Punti: " + player.getPunti());
                System.out.println("Posizione: " + player.getPos());
                System.out.println("Casella: "+t.getCell(player));
                System.out.println();
            }
            //new Scanner(System.in).nextLine();
        }
        Giocatore winner = t.chekWin(players);
        System.out.println("Il vincitore è: "+winner.getNome());
        System.out.println("Punti: "+winner.getPunti());
    }
}
