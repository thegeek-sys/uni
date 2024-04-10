public abstract class Pezzo2x2 extends Pezzo{
    public Pezzo2x2(int[][] shape) {
        super(shape);
    }

    public void rotate()
    {
        int[][] newShape = new int[2][2];
        newShape[0][0] = shape[1][0];
        newShape[0][1] = shape[0][0];

        newShape[1][0] = shape[1][1];
        newShape[1][1] = shape[0][1];

        shape = newShape;
    }
}
