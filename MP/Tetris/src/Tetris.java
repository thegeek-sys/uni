import java.util.Scanner;

public class Tetris {
    public static void main(String[] args) {
        Board b = new Board();
        b.genetarePiece();
        System.out.println(b);
        Scanner cmd = new Scanner(System.in);
        while (!b.getGameOver()) {
            System.out.print("Dove ti vuoi muovere?");
            String charin = cmd.nextLine();
            System.out.println();
            while (!charin.equals("a") && !charin.equals("s") && !charin.equals("d") && !charin.equals("q")) {
                System.out.println("Mossa invalida, usa asd per muoverti!");
                charin = cmd.nextLine();
            }
            switch (charin) {
                case "a" : b.moveLeft(); break;
                case "s" : b.moveDown(); break;
                case "d" : b.moveRight(); break;
                case "q" : System.exit(0); break;
            }
            System.out.println(b);
        }
    }
}
