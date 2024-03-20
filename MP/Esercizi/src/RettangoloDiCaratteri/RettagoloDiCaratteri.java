package RettangoloDiCaratteri;

public class RettagoloDiCaratteri {
    private int x,y,l,h;
    private char c;
    private char c1;
    public RettagoloDiCaratteri(int x, int y, int l, int h) {
        this.x = x;
        this.y = y;
        this.l = l;
        this.h = h;
        c = '*';
        c1 = '$';
    }

    public void setCarattere(char c, char c1) {
        this.c = c;
        this.c1 = c1;
    }

    public void setPos(int x, int y) {
        this.x = x;
        this. y = y;
    }

    public char[] getChars() {
        return new char[] {c, c1};
    }

    public void draw() {
        for (int i = 0; i <y+h; i++) {
            String s = "";
            for (int j = 0; j <x+l; j++) {
                if (x<=j && y<=i) {
                    s+=c;
                } else {
                    s+=" ";
                }
            }
            System.out.println(s);
        }
    }

    public void drawVerticalStripes() {
        for (int i = 0; i <y+h; i++) {
            String s = "";
            for (int j = 0; j <x+l; j++) {
                if (x<=j && y<=i) {
                    if (j%2 == 0) {
                        s+=c;
                    } else {
                        s+=c1;
                    }
                } else {
                    s+=" ";
                }
            }
            System.out.println(s);
        }
    }

    public void drawHorizontalStripes() {
        for (int i = 0; i <y+h; i++) {
            String s = "";
            for (int j = 0; j <x+l; j++) {
                if (x<=j && y<=i) {
                    if (j%2 == 0) {
                        s+=c;
                    } else {
                        s+=c1;
                    }
                } else {
                    s+=" ";
                }
            }
            System.out.println(s);
        }
    }

    public void drawChessboard() {
        for (int i = 0; i <y+h; i++) {
            String s = "";
            for (int j = 0; j <x+l; j++) {
                if (x<=j && y<=i) {
                    if (i%2 == 0) {
                        if (j%2 == 0) {
                            s+=c;
                        } else {
                            s+=c1;
                        }
                    } else {
                        if (j%2 == 1) {
                            s+=c;
                        } else {
                            s+=c1;
                        }
                    }

                } else {
                    s+=" ";
                }
            }
            System.out.println(s);
        }
    }

    public static void main(String[] args) {
        RettagoloDiCaratteri rect = new RettagoloDiCaratteri(2,2,4,3);
        rect.setCarattere('#', '.');
        rect.draw();
        rect.drawVerticalStripes();
        rect.drawHorizontalStripes();
        rect.drawChessboard();
        char[] c = rect.getChars();
        System.out.println(c);

    }
}
