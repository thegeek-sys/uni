package e13_06_23.memoria;

public class RemasteredLongPlay extends LongPlay {
    private int year;
    private String title;

    public RemasteredLongPlay(String title, String authors, int year) {
        super(title, authors);
        this.title = super.title+" "+year;
        this.authors=super.authors+" "+year;
        this.year = year;
    }

    @Override
    public String toString() {
        return super.toString()+" "+year;
    }
}
