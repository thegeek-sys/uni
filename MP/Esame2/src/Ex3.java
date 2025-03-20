import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class Ex3 {
    public static <T> Collection<T> filtraDoppioni(List<T> l) {
        ArrayList<T> res = new ArrayList<>();
        if (l.isEmpty() || l.size() == 1) return l;
        if (!l.getFirst().equals(l.get(1))) {
            res.add(l.getFirst());
        }
        res.addAll(filtraDoppioni(l.subList(1, l.size())));
        return res;
    }
}
