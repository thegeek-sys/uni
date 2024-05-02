package Treno;

public class PasseggeroNonAmmessoException extends Exception {
    public PasseggeroNonAmmessoException(String errorMsg) {
        super(errorMsg);
    }
}
