package casa.tetris.febbraio;

import java.util.Random;

public class Board {
	public static final int BOARD_WIDTH = 10;
	public static final int BOARD_HEIGHT = 6;
	public static final int POINTS_EACH_ROW = 100;
	private int score;
	private int[][] board = new int[BOARD_HEIGHT][BOARD_WIDTH];
	private int[][] currentPos = new int[4][2]; 
	private Pezzo p;
	//currentPos degli 1s nella board (ogni pezzo ha 4 blocchi)
			
	public Pezzo generatePiece() {
		Pezzo p = null;
		Random r = new Random();
		switch(r.nextInt(3)) {
		case 0: p = new Triangolo(4,0); break;//decido io che i pezzi
		case 1: p = new Quadrato(4,0); break;//vengono generati
		case 2: p = new ElleDx(4,0); break;// in y = 0; x = 4
		//case 3 ElleSx
		//case 4 I grande
		default: break;
		}
		//io ho che la current position è il punto in alto a sinistra della board quindi lo devo inizializzare
		int k = 0; //la riga di currentPos 
		for(int i=0; i<p.currentShape.length; i++) {//itero su righe
			for(int j=0; j<p.currentShape[0].length; j++) {//itero su colonne
				if(p.currentShape[i][j]==1) {//se c'è il pezzo
					currentPos[k][0] = p.getY() + i; //get.Y ti ritorna l'angolo in alto a sinistra e poi gli aggiungi
					currentPos[k][1] = p.getX() + j; // le coordinate, stessa storia per angolo a destra
					board[currentPos[k][0]][currentPos[k][1]] = 1;
					k++;
				}
			}
		}
		return p;
	}
	
	public void setPezzo(Pezzo p) {
		this.p = p;
	}
	
	public Pezzo getPezzo() {
		return p;
	}
	
	public int[][] getCurrentPosition(){
		return currentPos;
	}
	
	public int[][] getCurrentPos(Pezzo p){
		int[][] currentShape = p.getShape();
		//devo ciclare su shape, capire dove sono gli 1
		//e determinare una pos coerente nella Board
		//dentro currentPos
		int k = 0; //la riga di currentPos 
		for(int i=0; i<currentShape.length; i++) {//itero su righe
			for(int j=0; j<currentShape[0].length; j++) {//itero su colonne
				if(currentShape[i][j]==1) {//se c'è il pezzo
					currentPos[k][0] = p.getY() + i; //get.Y ti ritorna l'angolo in alto a sinistra e poi gli aggiungi
					currentPos[k][1] = p.getX() + j; // le coordinate, stessa storia per angolo a destra
					k++;
				}
			}
		}
		return currentPos;
	}
	
	public boolean canMoveDown(Pezzo p) {
		//cicli sulla shape di pezzo presa con getShape
		//poi se il pezzo è 1 e O il pezzo sotto è 1
		//o la board sotto è 1 torni false altrimenti true
		for(int i=0; i<currentPos.length;i++) {
			//cambia il +2 ma questo metodo è da modificare per prenderti la y massima
			if(board[currentPos[i][0]+2][currentPos[i][1]]==1)
			//se in posizione y+1 ho 1 allora non posso scendere
				return false;
		}
		return true;
	}
	
	public boolean canRotate(Pezzo p) {
		Pezzo pAppoggio = p;
		pAppoggio.rotate();
		int[][] currentPosAppoggio = this.getCurrentPos(pAppoggio);
		//ho lo screenshot della posizione che assumerebbe il pezzo 
		for(int i = 0; i< currentPosAppoggio.length;i++) {
			if(board[currentPosAppoggio[i][0]][currentPosAppoggio[i][1]]==1) {
				//se girando le nuove coordinate del pezzo incontrano un 1 sulla board
				return false;
			}
		}
		return true;}
	
	public boolean isInBounds(Pezzo p) {
		for(int i=0; i<currentPos.length;i++) {
			if(currentPos[i][0] > board.length-1) {//la y non deve essere maggiore della lunghezza della board
				return false;
			}
			if(currentPos[i][1]<0 || currentPos[i][1]>board[0].length-1) {
				//la x non deve essere negativa o maggiore della larghezza della board
				return false;
			}
		}
		return true;
		}	
	
	public void moveDown(Pezzo p) {
		//questa non è una copia! sono due variabili che si riferiscono allo stesso oggetto
		Pezzo pezzoAppoggio = copyPezzo(p);
		//System.out.println("il pezzo era in "+pezzoAppoggio.getY()+pezzoAppoggio.getX());
		if(canMoveDown(p)==true)
			p.down();//p.setY(p.getY()+1);//devi modificare y
		//System.out.println("il pezzo è in "+p.getY()+p.getX());
		placeRemovePiece(pezzoAppoggio,0);
		//però funziona per un solo pezzo...
		//this.board = new int[BOARD_HEIGHT][BOARD_WIDTH];
		this.currentPos = getCurrentPos(p);
		placeRemovePiece(p,1);		
	}
	
	public boolean landed(Pezzo p) {//aggiungere generate piece
		if(canMoveDown(p)==false && canRotate(p)==false && isInBounds(p)==true) {
			return true;
		}
		return false;
	}
	
	public void placeRemovePiece(Pezzo p, int r) {//se r = 1 place sennò remove
		if(isInBounds(p)==true) {
			for(int i=0; i<getCurrentPos(p).length;i++) {
				board[getCurrentPos(p)[i][0]][getCurrentPos(p)[i][1]]=r;
			}
		}
	}
	
	//this should be a deep copy
	public Pezzo copyPezzo(Pezzo p) {
		//copy shape
		int[][] otherShape = new int[p.currentShape.length][p.currentShape[0].length];
		for(int i=0; i<p.currentShape.length;i++) {
			for(int j=0;j<p.currentShape[0].length;j++) {
				otherShape[i][j] = p.currentShape[i][j];
			}
		}
		
		if(p.getClass().getSimpleName().equals("Triangolo")) {
			Pezzo pCopy = new Triangolo(p.getX(),p.getY());
			pCopy.currentShape = otherShape;
			return pCopy;
		} else if(p.getClass().getSimpleName().equals("Quadrato")) {
			Pezzo pCopy = new Quadrato(p.getX(),p.getY());
			pCopy.currentShape = otherShape;
			return pCopy;
		} else if(p.getClass().getSimpleName().equals("ElleDx")) {
			Pezzo pCopy = new ElleDx(p.getX(),p.getY());
			pCopy.currentShape = otherShape;
			return pCopy;
		} else return null;
		
		/*
		switch(p.getClass().getName()) {
		case "Triangolo": Pezzo pCopy = new Triangolo(4,0); break;//decido io che i pezzi
		case "Quadrato": Pezzo pCopy = new Quadrato(4,0); break;//vengono generati
		case "ElleDx": Pezzo pCopy = new ElleDx(4,0); break;// in y = 0; x = 4
		//case 3 ElleSx
		//case 4 I grande
		default: break;
		}
		*/
	}
	
	public String toString() {
		String s = "";
		for(int i=0; i<board.length; i++) {
			for(int j=0; j<board[0].length;j++) {
				s = s + board[i][j];
				if(j==board[0].length-1) s = s +"\n";
			}
		}
		return s;
	}
	
}
