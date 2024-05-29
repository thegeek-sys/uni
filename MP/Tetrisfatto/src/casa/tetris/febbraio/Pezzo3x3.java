package casa.tetris.febbraio;

public abstract class Pezzo3x3 extends Pezzo{
	
	public Pezzo3x3(int[][] shape, int x, int y) {
		super(shape, x, y);
	}
	
	public void rotate() {
		//1 2 3
		//4 5 6
		//7 8 9
		//ruoto di 90 clockwise
		//7 4 1
		//8 5 2
		//9 6 3
		int[][] newShape = new int[3][3];
		newShape[0][0]=currentShape[2][0];
		newShape[0][1]=currentShape[1][0];
		newShape[0][2]=currentShape[0][0];
		newShape[1][0]=currentShape[2][1];
		newShape[1][2]=currentShape[0][1];
		newShape[2][0]=currentShape[2][2];
		newShape[2][1]=currentShape[1][2];
		newShape[2][2]=currentShape[0][2];
		currentShape=newShape;
	}

}
