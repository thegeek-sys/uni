package e13_06_23_1.gestione;

import java.util.ArrayList;

public class CollanaFumetti {
    private String titolo;
    private String publisher;
    private ArrayList<Volume> volumi;

    public CollanaFumetti(String titolo, String publisher) {
        this.titolo = titolo;
        this.publisher = publisher;
    }

    public String getTitolo() {
        return titolo;
    }

    public String getPublisher() {
        return publisher;
    }

    public ArrayList<Volume> getVolumi() {
        return volumi;
    }
}
