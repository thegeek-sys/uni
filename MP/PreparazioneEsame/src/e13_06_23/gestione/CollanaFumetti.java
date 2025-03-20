package e13_06_23.gestione;

import java.util.ArrayList;

public class CollanaFumetti {
    private String titolo;
    private String publisher;
    private ArrayList<Volume> volumi;

    public CollanaFumetti(String titolo, String publisher) {
        this.titolo = titolo;
        this.publisher = publisher;
        volumi = new ArrayList<>();
    }

    public ArrayList<Volume> getVolumi() {
        return volumi;
    }
}
