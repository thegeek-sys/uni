public abstract class Pezzo {
    private int x, y;
    protected int[][] shape;

    public Pezzo(int[][] shape) {
        this.shape = shape;
        x = 0;
        y = 0;
    }

    public int getX() { return x; }
    public int getY() { return y; }
    public void setX(int x) { this.x = x; }
    public void setY(int y) { this.y = y; }

    public int[][] getShape() { return shape; }

    public abstract void rotate();
}
