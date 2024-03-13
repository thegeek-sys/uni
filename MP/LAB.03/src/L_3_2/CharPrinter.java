package L_3_2;

public class CharPrinter {
    public static void main(String[] args) {
        String s;
        if (args.length == 0) {
            java.util.Scanner input = new java.util.Scanner(System.in);
            s = input.nextLine();
        } else {
            s = args[0];
        }
        for (int i = 0; i < s.length(); i++) {
            System.out.println(s.charAt(i));
        }
    }
}
