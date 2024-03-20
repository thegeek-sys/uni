package L_3_1;

public class ContaParole {
    private String[] testo;
    private String w;

    public ContaParole (String testo, String w) {
        this.w = w;
        this.testo = testo.split(" ");
    }

    public int getCount() {
        int c = 0;
        for (int i=0; i<testo.length; i++) {
            if (testo[i].equals(w)) c++;
        }
        return c;
    }

    public static void main(String[] args) {
        ContaParole conteggio = new ContaParole("ciao caro come stai", "ciao");
        System.out.println(conteggio.getCount());
    }

}
