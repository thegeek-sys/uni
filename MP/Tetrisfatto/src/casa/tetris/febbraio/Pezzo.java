package casa.tetris.febbraio;

public abstract class Pezzo {
	protected int[][] currentShape;
	//x e y sono la posizione del pezzo assumiamo angolo alto a sinistra
	private int x;
	private int y;
	
	public Pezzo(int[][] shape, int x, int y) {
		currentShape = shape;
		this.x = x;
		this.y = y;
	}
	
	public int left() {return --x;}
	public int right() {return ++x;}
	public int down() {return ++y;}
	
	public int getX() {return x;}
	public int getY() {return y;}
	public int[][] getShape() {return currentShape;}
	
	public void setX(int x) {this.x = x;}
	public void setY(int y) {this.y = y;}
	
	public abstract void rotate();
	
	@Override
	public String toString() {
		String s="";
		for(int i=0; i<currentShape.length;i++) {
			for(int j =0; j<currentShape[0].length;j++)
				s = s+currentShape[i][j]+" ";
			s = s + "\n";
		}
		return s;
	}
}
