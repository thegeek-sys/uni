package Treno;

public class LocomotiveMultipleException extends Exception {
    public LocomotiveMultipleException() {
        super("Un treno non può avere più locomotive");
    }
}
