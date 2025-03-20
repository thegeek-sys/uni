package e13_06_23_1.heap;

public class Main {
    public static void main(String[] args) {
        int k;
        String s;
        LongPlay lp = new LongPlay("Elemental", "Tears for fears");
        LongPlay rlp = new RemasteredLongPlay("Elemental", "Tears for fears", 2023);
        String result = ((LongPlay)rlp).toString();
        System.out.println(LongPlay.getNumberOfLongPlay());
        System.out.println();
    }
}
