package casa.tetris.febbraio;

public class ElleDx extends Pezzo3x3 {
	public ElleDx(int x, int y) {
		super(new int[][]{
				{1,1,1},
				{0,0,1},
				{0,0,0},
				}, x, y);
	}
}
