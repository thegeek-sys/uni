package e19_06_24.ricorsivo;

import java.util.ArrayList;
import java.util.List;

public class Ex3 {
    public static <T> List<T>  getSenzaAdiacenti(List<T> doppioni) {
        if (doppioni.size() <= 1) return doppioni;
        if (doppioni.getFirst().equals(doppioni.get(1))) doppioni.remove(doppioni.get(1));
        getSenzaAdiacenti(doppioni.subList(1,doppioni.size()));
        return doppioni;

    }

    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<>();
        a.add(2);
        a.add(2);
        a.add(1);
        a.add(1);
        a.add(5);
        a.add(5);
        a.add(4);
        a.add(4);
        a.add(6);
        a.add(5);
        a.add(5);
        a.add(2);
        System.out.println(getSenzaAdiacenti(a));
    }
}
