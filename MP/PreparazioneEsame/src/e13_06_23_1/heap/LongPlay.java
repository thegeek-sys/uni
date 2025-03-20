package e13_06_23_1.heap;

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

    public static int getNumberOfLongPlay() {
        return numberOfLongPlay;
    }
}
