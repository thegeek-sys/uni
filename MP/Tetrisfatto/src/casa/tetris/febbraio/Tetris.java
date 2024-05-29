package casa.tetris.febbraio;

import java.util.Scanner;


public class Tetris {
	
	public static void main(String[] args)
	{
		Board b = new Board();
		b.setPezzo(b.generatePiece());
		b.placeRemovePiece(b.getPezzo(),1);
		boolean gameover=false;
		Scanner input=new Scanner(System.in);
		while (!gameover)
		{
			String cmd=input.next();
			switch (cmd)
			{
			case "l":/**/break;
			case "r":/**/break;
			case "d":b.moveDown(b.getPezzo());
			  	     System.out.println(b.toString());
			  	     break;
			case "q":gameover=true;break;
			default: break;
			}
			; 
		}
		input.close();
	}
	
}
