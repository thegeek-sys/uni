package Treno;

public class PostiNonDisponibiliException extends Exception {
    public PostiNonDisponibiliException(String errorMsg) {
        super(errorMsg);
    }
}
