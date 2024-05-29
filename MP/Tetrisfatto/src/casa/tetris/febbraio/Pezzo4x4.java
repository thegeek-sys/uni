package casa.tetris.febbraio;

public abstract class Pezzo4x4 extends Pezzo {
	
	public Pezzo4x4(int[][] shape, int x, int y) {
		super(shape, x, y);
	}
	
	public void rotate() {
		//1  2   3  4
		//5  6   7  8
		//9  10 11 12
		//13 14 15 16
		//ruoto di 90 clockwise
		//13  9  5  1
		//14  10 6  2
		//15  11 7  3
		//16  12  8 4
		int[][] newShape = new int[4][4];
		newShape[0][0]=currentShape[3][0];
		newShape[0][1]=currentShape[2][0];
		newShape[0][2]=currentShape[1][0];
		newShape[0][3]=currentShape[0][0];
		newShape[1][0]=currentShape[3][1];
		newShape[1][1]=currentShape[2][1];
		newShape[1][2]=currentShape[1][1];
		newShape[1][3]=currentShape[0][1];
		//....
		newShape[3][3]=currentShape[0][3];
		currentShape=newShape;
	}

}
