import java.util.Arrays;

public class Ex3 {
    public static <T extends Comparable<T>> T getValoreMax(T[] valori) {
        if (valori.length == 0) return null;
        if (valori.length == 1) return valori[0];
        if (valori[0].compareTo(valori[1]) >= 0) {
            valori[1] = valori[0];
        }
        T[] nValori = Arrays.copyOfRange(valori, 1, valori.length);
        return getValoreMax(nValori);
    }

    public static void main(String[] args) {
        Integer[] valori = new Integer[] {2, 2, 1,  1,  5,  5, 4,  4,  6,  5, 5, 2};
        System.out.println(Arrays.toString(valori));
        System.out.println(getValoreMax(valori));
    }
}
