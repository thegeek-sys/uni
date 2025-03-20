package e13_07_23.ricorsione;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Ex3 {
    public static <T> List<T> invertiFiltraLista(List<T> lista, HashSet<T> set) {
        if (lista.isEmpty()) return lista;
        List<T> c = new ArrayList<>();
        if (!set.contains(lista.getLast())) {
            c.add(lista.getLast());
        }
        c.addAll(invertiFiltraLista(lista.subList(0, lista.size()-1), set));
        return c;
    }

    public static void main(String[] args) {
        ArrayList<String> a = new ArrayList<>();
        a.add("mario");
        a.add("luigi");
        a.add("luigi");
        a.add("luigi");
        a.add("peach");
        a.add("peach");
        a.add("mario");
        a.add("toad");
        HashSet<String> s = new HashSet<>();
        s.add("mario");
        s.add("luigi");
        System.out.println(a);
        System.out.println(invertiFiltraLista(a, s));
    }
}
