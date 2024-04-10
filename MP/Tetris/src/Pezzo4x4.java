public abstract class Pezzo4x4 extends Pezzo {
    public Pezzo4x4(int[][] shape)
    {
        super(shape);
    }
    public void rotate()
    {
        int[][] newShape = new int[4][4];
        newShape[0][0] = shape[3][0];
        newShape[0][1] = shape[2][0];
        newShape[0][2] = shape[1][0];
        newShape[0][3] = shape[0][0];

        newShape[1][0] = shape[3][1];
        newShape[1][1] = shape[2][1];
        newShape[1][2] = shape[1][1];
        newShape[1][3] = shape[0][1];

        newShape[2][0] = shape[3][2];
        newShape[2][1] = shape[2][2];
        newShape[2][2] = shape[1][2];
        newShape[2][3] = shape[0][2];

        newShape[3][0] = shape[3][3];
        newShape[3][1] = shape[2][3];
        newShape[3][2] = shape[1][3];
        newShape[3][3] = shape[0][3];

        shape = newShape;
    }
}