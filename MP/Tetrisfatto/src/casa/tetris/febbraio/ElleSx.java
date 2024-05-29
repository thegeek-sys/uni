package casa.tetris.febbraio;

public class ElleSx extends Pezzo3x3 {
	public ElleSx(int x, int y) {
		super(new int[][]{
				{1,1,1},
				{1,0,0},
				{0,0,0},
				}, x, y);
	}
}
