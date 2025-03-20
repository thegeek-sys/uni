package memoria;

public class Main {
    Object o;
    public static void main(String[] args)	{
        int k;
        String s;
        LongPlay lp=new LongPlay("Albedo 0,39","Vangelis");
        LongPlay rlp=new RemasteredLongPlay("Albedo 0,39","Vangelis",2024);
        String result=((LongPlay)rlp).toString();
        System.out.println(LongPlay.numerbOfLongPlay);
        System.out.println();
    }
}

