import java.util.Random;

public class Board {
    public final static int WIDTH = 10;
    public final static int HEIGHT = 6;
    private int[][] board = new int[HEIGHT][WIDTH];
    private Pezzo p;
    private boolean gameOver = false;

    public void genetarePiece() {
        Random r = new Random();
        int randPiece = r.nextInt(7);
        p = switch (randPiece) {
            case 0 -> new Barra();
            case 1 -> new ElleDx();
            case 2 -> new ElleSx();
            case 3 -> new Quadrato();
            case 4 -> new Triangolo();
            case 5 -> new ZigZagDx();
            case 6 -> new ZigZagSx();
            default -> throw new IllegalStateException("Unexpected value: " + randPiece);
        };

        int randRot = r.nextInt(1,4);
        for (int rot=0; rot<randRot; rot++) {
            p.rotate();
        }

        int[][] currShape = p.getShape();
        for (int y=0; y<currShape.length; y++) {
            for (int x=0; x<currShape[0].length; x++) {
                board[y][x] = currShape[y][x];
            }
            p.setY(p.getY()+1);
        }
    }

    public void moveDown() {
        if (p.getY()+1<=HEIGHT-1){
            int[][] newBoard = copyBoard();
            for (int w = 0; w < WIDTH; w++) {
                board[0][w] = 0;
            }
            for (int y = 1; y < HEIGHT; y++) {
                for (int x = 0; x < WIDTH; x++) {
                    board[y][x] = newBoard[y - 1][x];
                }
            }
            p.setY(p.getY() + 1);
        } else {
            gameOver = true;
        }
    }

    public void moveRight() {
        if (p.getX()+p.getShape()[0].length+1<=WIDTH-1){
            int[][] newBoard = copyBoard();
            for (int h = 0; h < HEIGHT; h++) {
                board[h][0] = 0;
            }
            for (int y = 0; y < HEIGHT; y++) {
                for (int x = 1; x < WIDTH; x++) {
                    board[y][x] = newBoard[y][x - 1];
                }
            }
            p.setX(p.getX() + 1);
        }
    }

    public void moveLeft() {
        if (p.getX()-1>=0){
            int[][] newBoard = copyBoard();
            for (int h = 0; h < HEIGHT; h++) {
                board[h][WIDTH - 1] = 0;
            }
            for (int y = 0; y < HEIGHT; y++) {
                for (int x = 0; x < WIDTH - 1; x++) {
                    board[y][x] = newBoard[y][x + 1];
                }
            }
            p.setX(p.getX()-1);
        }
    }

    public int[][] copyBoard() {
        int[][] copiedBoard = new int[HEIGHT][WIDTH];
        for(int y=0; y<HEIGHT; y++) {
            for(int x=0; x<WIDTH; x++) {
                copiedBoard[y][x] = board[y][x];
            }
        }
        return copiedBoard;
    }

    public int[][] getBoard() { return board; }
    @Override
    public String toString() {
        String s = "";
        for (int y=0; y<HEIGHT; y++) {
            for (int x=0; x<WIDTH; x++) {
                s += board[y][x];
            }
            s += "\n";
        }
        return s;
    }

    public boolean getGameOver() {
        return gameOver;
    }
}
