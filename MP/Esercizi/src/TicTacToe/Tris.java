package TicTacToe;
import java.util.Scanner;

public class Tris {
    private ScacchieraTris board;
    private String p1, p2;
    private int turn;
    public Tris(String p1, String p2) {
        board = new ScacchieraTris();
        this.p1 = p1;
        this.p2 = p2;
        turn = 0;
    }

    public String getCurPlay() {
        return turn%2==0 ? p1: p2;
    }

    public boolean checkWin() {
        for (int i=1; i<=7; i+=3) {
            if (!board.getScacchiera(i).equals(" ") && board.getScacchiera(i).equals(board.getScacchiera(i+1)) && board.getScacchiera(i+1).equals(board.getScacchiera(i+2))) {
                return true;
            }
        }

        for (int i=1; i<=3; i++) {
            if (!board.getScacchiera(i).equals(" ") && board.getScacchiera(i).equals(board.getScacchiera(i + 3)) && board.getScacchiera(i + 3).equals(board.getScacchiera(i + 6))) {
                return true;
            }
        }

        if (!board.getScacchiera(1).equals(" ") && board.getScacchiera(1).equals(board.getScacchiera(5)) && board.getScacchiera(5).equals(board.getScacchiera(9))) {
            return true;
        } else if (!board.getScacchiera(3).equals(" ") && board.getScacchiera(1).equals(board.getScacchiera(5)) && board.getScacchiera(5).equals(board.getScacchiera(7))) {
            return true;
        }

            return false;
    }

    public void setMove(int pos) {
        board.setScacchiera(turn%2==0 ? "X": "O", pos);
    }

    public boolean checkPos(int pos) {
        return board.getScacchiera(pos).equals(" ");
    }

    public void stampa() {
        board.stampa();
    }

    public int getTurn() { return turn; }

    public void setTurn() { turn++; }

    //public void resetTris() {

    //}

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Nome player 1: ");
        String p1 = input.nextLine();
        System.out.println("Nome player 2: ");
        String p2 = input.nextLine();
        Tris game = new Tris(p1, p2);

        while (game.getTurn() < 9) {
            int tile;
            do {
                game.stampa();
                System.out.println("E' il turno di: "+game.getCurPlay());
                tile = input.nextInt();
            } while (!game.checkPos(tile));
            game.setMove(tile);
            if (game.checkWin()) {
                System.out.println("HAI VINTO "+game.getCurPlay()+"!");
                break;
            }
            game.setTurn();


        }
    }


}
