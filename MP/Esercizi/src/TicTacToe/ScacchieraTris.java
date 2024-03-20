package TicTacToe;

public class ScacchieraTris {
    private String[][] board = new String[][] { {" ", " ", " "}, { " ", " ", " " }, { " ", " ", " " } };
    public void stampa() {
        for (int i=0; i<board.length; i++) {
            for (int j=0; j<board[0].length; j++) {
                System.out.print("| "+board[i][j]+" |");
            }
            System.out.println();
        }
    }

    public void setScacchiera(String player, int pos) {
        switch (pos) {
            case 1 -> board[0][0] = player;
            case 2 -> board[0][1] = player;
            case 3 -> board[0][2] = player;
            case 4 -> board[1][0] = player;
            case 5 -> board[1][1] = player;
            case 6 -> board[1][2] = player;
            case 7 -> board[2][0] = player;
            case 8 -> board[2][1] = player;
            case 9 -> board[2][2] = player;
        };
    }

    public String getScacchiera(int pos) {
        return switch (pos) {
            case 1 -> board[0][0];
            case 2 -> board[0][1];
            case 3 -> board[0][2];
            case 4 -> board[1][0];
            case 5 -> board[1][1];
            case 6 -> board[1][2];
            case 7 -> board[2][0];
            case 8 -> board[2][1];
            case 9 -> board[2][2];
            default -> "pippo";
        };
    }

    public void clearBoard() {
        for (int i=0; i<board.length; i++) {
            for (int j=0; j<board[0].length; j++) {
                board[i][j] = " ";
            }
        }
    }

    public static void main(String[] args) {
        ScacchieraTris s = new ScacchieraTris();
        s.stampa();
        s.setScacchiera("X", 1);
        s.stampa();
    }
}
