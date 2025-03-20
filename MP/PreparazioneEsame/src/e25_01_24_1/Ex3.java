package e25_01_24_1;

import java.util.HashMap;
import java.util.Map;

public class Ex3 {
    public static <T> Map<T, Integer> contaElementiMatrice(T[][] matrix, int x, int y, boolean goingDown) {
        if (matrix.length == 0) return null;
        if (y == 0 && x == 0) {
            HashMap<T, Integer> map = new HashMap<>();
            map.put(matrix[y][x], 1);
            return map;
        }
        if (matrix.length-1 == y && matrix[0].length-1 == x ) {
            HashMap<T, Integer> map = new HashMap<>();
            map.put(matrix[y][x], 1);
            return map;
        }
        Map<T, Integer> mapDown = new HashMap<>();
        Map<T, Integer> mapUp = new HashMap<>();
        if (goingDown) {
            if (x == matrix[0].length-1) {
                mapDown = contaElementiMatrice(matrix, 0, y+1, goingDown);
            } else {
                mapDown = contaElementiMatrice(matrix, x+1, y, goingDown);
            }
            mapDown.put(matrix[y][x], mapDown.getOrDefault(matrix[y][x], 0)+1);

        }
        if (x == matrix[0].length/2 && y == matrix.length/2) {
            goingDown = false;
            mapDown.put(matrix[y][x], mapDown.get(matrix[y][x])-1);
        }
        if (!goingDown) {
            if (x == 0) {
                mapUp = contaElementiMatrice(matrix, matrix[0].length-1, y-1, goingDown);
            } else {
                mapUp = contaElementiMatrice(matrix, x-1, y, goingDown);
            }
            mapUp.put(matrix[y][x], mapUp.getOrDefault(matrix[y][x], 0)+1);

        }
        for (Map.Entry<T, Integer> e : mapUp.entrySet())
            mapDown.merge(e.getKey(), e.getValue(), Integer::sum);
        return mapDown;
    }
    public static <T> Map<T, Integer> contaElementiMatrice(T[][] matrix) {
        return contaElementiMatrice(matrix, matrix[0].length/2, matrix.length/2, true);
    }

    public static void main(String[] args) {
        Integer[][] integer = {{1,2,1,5},{1,4,1,3},{2,1,1,5}};
        System.out.println(contaElementiMatrice(integer));
    }
}
