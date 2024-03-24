package L_3_6;

public class L_3_6 {
    public static void fibonacciN (int srt, int end, int N) {
        System.out.print(srt+", "+end);

        int result = srt+end;
        for (int i=0; i<N; i++) {
            System.out.print(", "+result);
            srt = end;
            end = result;
            result = srt+end;
        }
    }

    public static void main(String[] args) {
        fibonacciN(2,3,6);
    }
}
