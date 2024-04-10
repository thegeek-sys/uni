public abstract class Pezzo3x3 extends Pezzo{
    public Pezzo3x3(int[][] shape) {
        super(shape);
    }

    public void rotate()
    {
        int[][] newShape = new int[3][3];
        newShape[0][0] = shape[2][0];
        newShape[0][1] = shape[1][0];
        newShape[0][2] = shape[0][0];

        newShape[1][0] = shape[2][1];
        newShape[1][1] = shape[1][1];
        newShape[1][2] = shape[0][1];

        newShape[2][0] = shape[2][2];
        newShape[2][1] = shape[1][2];
        newShape[2][2] = shape[0][2];

        shape = newShape;
    }
}
