package L_8_2;

import java.util.ArrayList;
import java.util.HashMap;

public class MultiMappa {
    private HashMap<Integer, ArrayList<String>> map;

    public ArrayList<String> get(int k) {
        return map.getOrDefault(k, new ArrayList<String>());
    }

}
