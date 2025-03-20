package e13_06_23.memoria;

public class LongPlay {
    private static int numberOfLongPlay;
    protected String title;
    protected String authors;

    public LongPlay(String title, String authors) {
        this.title=title;
        this.authors=authors;
        numberOfLongPlay++;
    }

    @Override
    public String toString() {
        return title+" "+authors;
    }
}
