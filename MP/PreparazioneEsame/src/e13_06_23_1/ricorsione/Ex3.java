package e13_06_23_1.ricorsione;

import java.util.ArrayList;
import java.util.List;

public class Ex3 {
    public static <T> List<T> filtraDoppioni(List<T> l) {
        if (l.isEmpty()) return null;
        if (l.size() == 1) return l;
        if (l.getFirst().equals(l.get(1))) {
            l.removeFirst();
        }
        filtraDoppioni(l.subList(1, l.size()));
        return l;
    }

    public static void main(String[] args) {
        ArrayList<String> a = new ArrayList<>();
        a.add("mario");
        a.add("luigi");
        a.add("luigi");
        a.add("peach");
        a.add("peach");
        System.out.println(filtraDoppioni(a));
    }
}
