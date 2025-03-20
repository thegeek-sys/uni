package memoria;

public class LongPlay {
    public static int numerbOfLongPlay;
    protected String title;
    protected String authors;
    public LongPlay(String title){
        this(title,null);
    }
    public LongPlay(String title, String authors){
        this.title=title;
        this.authors=authors;
        numerbOfLongPlay++;
    }
    @Override
    public String toString(){
        return title+" "+authors;
    }
}

