package casa.tetris.febbraio;

public abstract class Pezzo2x2 extends Pezzo {
	
	Pezzo2x2(int[][] shape, int x, int y){
		super(shape, x, y);
	}
	
	public void rotate()
	{
		//  1  2
		//  3  4
 		//  90 gradi clockwise
		//  3 1
		//  4 2
		int[][] newShape=new int[2][2];
		newShape[0][0]=currentShape[1][0];
		newShape[0][1]=currentShape[0][0];
		newShape[1][0]=currentShape[1][1];
		newShape[1][1]=currentShape[0][1];
		currentShape=newShape;
		}
}
