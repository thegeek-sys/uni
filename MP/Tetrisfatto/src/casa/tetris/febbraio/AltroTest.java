package casa.tetris.febbraio;

public class AltroTest {
	
	public static void main(String[] args) {
		//int[][] vector = {{1,2,3,4},{5,6,7,8}};
		
		
		Board b = new Board();
		System.out.println(b.toString());
		b.setPezzo(b.generatePiece());
		b.placeRemovePiece(b.getPezzo(),1);
		
		System.out.println(b.getPezzo().toString());
		
		for(int i=0;i<b.getCurrentPosition().length;i++) {
			System.out.println(""+b.getCurrentPosition()[i][0]+b.getCurrentPosition()[i][1]);
		}
		
		//System.out.println(b.canMoveDown(b.getPezzo()));
		
		System.out.println(b.toString());
		//b.placeRemovePiece(b.getPezzo(), 0);
		//System.out.println(b.toString());
		//b.placeRemovePiece(b.getPezzo(), 1);
		//System.out.println(b.toString());
		b.moveDown(b.getPezzo());
		System.out.println(b.toString());
		b.moveDown(b.getPezzo());
		System.out.println(b.toString());
		//b.moveDown(b.getPezzo());
		//System.out.println(b.toString());
		
		//System.out.println(b.getPezzo().getClass().getSimpleName());
	}
}
