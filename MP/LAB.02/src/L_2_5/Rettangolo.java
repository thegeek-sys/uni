package L_2_5;

public class Rettangolo {
    private int x,y,x1,y1;
    private Colore c;

    public Rettangolo(int x, int y, int w, int h) {
        this.x = x;
        this.y = y;
        x1 = x+w;
        y1 = y+h;
        c = new Colore();
    }

    public void trasla(int xi, int yi) {
        x+=xi;
        x1+=xi;
        y+=yi;
        y1+=yi;
    }

    public void setColore(int r, int g, int b) {
        c = new Colore(r,g,b);
    }

    public String getColore() {
        return c.display();
    }

    public String toString() {
        return "("+x+", "+y+")-("+x1+", "+y1+")";
    }
}
