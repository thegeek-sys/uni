package L_8_2;

import java.util.*;

public class MultiMappa {
    private HashMap<Integer, ArrayList<String>> map;

    public ArrayList<String> get(int k) {
        return map.getOrDefault(k, new ArrayList<String>());
    }

    public void put(int k, String s) {
        map.merge(k, new ArrayList<String>(List.of("Orange")), (oldValue, newValue) -> {
            oldValue.addAll(newValue);
            return oldValue;
        });
    }

    public HashSet<Integer> keySet() {
        return (HashSet<Integer>)map.keySet();
    }

    public ArrayList<ArrayList<String>> values() {
        return (ArrayList<ArrayList<String>>) map.values();
    }

    public HashSet<ArrayList<String>> valueSet() {
        return (HashSet<ArrayList<String>>)map.values();
    }

    public ArrayList<String> sortedValues() {
        ArrayList<String> list = new ArrayList<String>();
        for (List<String> l : map.values()) {
            l.sort(String::compareTo);
            list.addAll(l);
        }
        return list;
    }

}
