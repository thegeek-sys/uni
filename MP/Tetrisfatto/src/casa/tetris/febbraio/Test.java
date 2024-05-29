package casa.tetris.febbraio;

import java.util.Random;

public class Test {

	public static void main(String[] args) {
		int[][] x = new int[][] {{0,1},{2,3},{4,5}};
		
		int y = x.length;//nrow
		int z = x[0].length;//ncol
		System.out.println(y+" "+z);
		
		System.out.println(new Triangolo(1,1).toString());
		
		Random r = new Random();
		System.out.println(r.nextInt(3));
		
		//Board b = new Board();
		//Pezzo pezzo = b.generatePiece();
		//System.out.println(pezzo.toString());
		
		int[][] q = new int[3][2];
		q[0][1] = 1;
		String s="";
		for(int i=0; i<q.length;i++) {
			for(int j =0; j<q[0].length;j++)
				s = s+q[i][j]+" ";
			s = s + "\n";
		}
		System.out.println(s);

	}
}
