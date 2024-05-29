package casa.tetris.febbraio;

public class Triangolo extends Pezzo3x3 {
	public Triangolo(int x, int y) {
		super(new int[][] 
				{{0,1,0},
				{1,1,1},
				{0,0,0}},x,y);
	}
}