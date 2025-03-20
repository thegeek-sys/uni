package e13_06_23.memoria;

public class Main {
    public static void main(String[] args) {
        int k;
        String s;
        LongPlay lp = new LongPlay("Elemental", "Tears for fears");
        LongPlay rlp = new RemasteredLongPlay("Elemental", "Tears for fears", 2023);
        String result = ((LongPlay)rlp).toString();
        // https://drive.google.com/file/d/1QjZwERJwnOyUuZhPvTbVQjnA4Q9BxuUF/view?usp=drive_link
    }
}
