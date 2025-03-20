package e08_09_23.ricorsione;

import java.util.HashSet;
import java.util.Set;

public class Ex3 {
    public static <T extends EsseriViventi> HashSet<EsseriViventi> ciSonoEsseriViventiNelVicinatoDiRaggioR(T[][] matrix, Set<T> set, int x, int y, int r) {
        HashSet<EsseriViventi> s = new HashSet<>();
        for (int i=0; i<matrix.length; i++) {
            for (int j=0; j<matrix[0].length; j++) {
                if (Math.sqrt(Math.pow(Math.abs(i+y), 2)+Math.pow(Math.abs(j+x), 2)) <= r && set.contains(matrix[i][j])) {
                    s.add(matrix[i][j]);
                }
            }
        }
        return s;
    }
}
