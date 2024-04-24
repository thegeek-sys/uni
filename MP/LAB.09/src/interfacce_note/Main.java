package interfacce_note;
import java.rmi.MarshalException;
import java.util.NavigableSet;
import java.util.TreeSet;
import java.util.function.*;
// import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        Function<Double,Double> e2_4_1 = x -> x*x;
        e2_4_1.apply(4.0);

        Consumer<String> e2_4_2 = s -> System.out.println(s);
        e2_4_2.accept("Hello world");
        Consumer<String> e2_4_2_1 = System.out::println;
        e2_4_2_1.accept("Hello world");

        /*
        Si definisca in una riga una variabile del tipo di un’interfaccia
        funzionale standard del package java.util.function e le si associ una lambda
        (non un riferimento a metodo) che, prendendo in input una stringa e
        un intero, restituisca un booleano che verifica se la stringa `e della lunghezza
        pari all’intero fornito in input. Si scriva quindi una seconda riga per invocare il
        metodo dell’interfaccia.
        */
        BiPredicate<String, Integer> e2_4_3 = (s, i) -> s.length()==i;
        e2_4_3.test("ciao", 4);


        /*
        Si definisca in una riga una variabile del tipo di un’interfaccia
        funzionale standard del package java.util.function e le si associ una lambda
        (non un riferimento a metodo) che, senza prendere nulla in input, restituisca un
        numero intero casuale. Si scriva quindi una seconda riga per invocare il metodo
        dell’interfaccia.
        */
        Supplier<Integer> e2_4_4 = () -> (int)(Math.random()*Integer.MAX_VALUE);
        e2_4_4.get();


        /*
        Si definisca in una riga una variabile del tipo di un’interfaccia
        funzionale standard del package java.util.function e le si associ una lambda
        (non un riferimento a metodo) che, prendendo in input una stringa, restituisca
        un booleano che verifica se la stringa è vuota oppure no. Si scriva quindi una
        seconda riga per invocare il metodo dell’interfaccia.
        */
        Predicate<String> e2_4_5 = s -> s.isEmpty();
        e2_4_5.test("ciao");
        /* il compilatore sovraccarica (overloading) il metodo isEmpty
        boolean isEmpty(String s) {
            return.isEmpty();
        }
        */
        Predicate<String> e2_4_5_1 = String::isEmpty;
        e2_4_5_1.test("ciao");


        /*
        Progettare un’interfaccia funzionale ElaboraStringhe che
        esponga un metodo elabora il quale, data in input una stringa, restituisca
        un’altra stringa. Scrivere quindi le seguenti espressioni lambda da assegnare
        alla riga ElaboraStringhe e = in modo tale che:
        - l’espressione restituisca la rappresentazione sotto forma di stringa della
          lunghezza della stringa in input;
        - l’espressione restituisca i primi 5 caratteri della stringa o, se pi`u piccola,
          la stringa per intero.
        */
        ElaboraStringhe e1 = (s) -> String.valueOf(s.length());
        e1.elabora("ciao");
        ElaboraStringhe e2 = (s) -> s.length()>5 ? s.substring(0,4) : s;
        e2.elabora("pippo");


        /*
        Progettare un’interfaccia funzionale VerificaStringhe che
        esponga un metodo verifica il quale, date in input due stringhe s1 e s2, resti-
        tuisca un booleano. Scrivere quindi le seguenti espressioni lambda da assegnare
        alla riga VerificaStringhe v = in modo tale che:
        - l’espressione restituisca true se s2 `e contenuto in s1, false altrimenti;
        - l’espressione restituisca true se la lunghezza di s1 `e maggiore di quella di
          s2 ed s1 non contiene s2 come suffisso.
        */
        VerificaStringhe v1 = (s1, s2) -> s1.contains(s2);
        // VerificaStringhe v1 = String::contains;
        VerificaStringhe v2 = (s1, s2) -> s1.length()>s2.length() && !(s1.endsWith(s2));


        /*
        Progettare un’interfaccia funzionale FunzioneSuInsieme che
        esponga un metodo applica il quale, dato in input un insieme di interi e un
        intero k, restituisca un intero. Scrivere quindi le seguenti espressioni lambda da
        assegnare alla riga FunzioneSuInsieme f = in modo tale che:
        - l’espressione restituisca la somma dei valori ≤ k nell’insieme;
        - l’espressione restituisca il minimo valore nell’insieme; null se l’insieme `e
          vuoto.
        */
        FunzioneSuInsieme f1 = (t, k) -> {
            int sum = 0;
            NavigableSet<Integer> subTree = t.headSet(k, true);
            for(int i : subTree) {
                sum += i;
            }
            // subTree.forEach(x -> sum+=x);
            return sum;
        };
        FunzioneSuInsieme f2 = (t, k) -> t.getFirst();
    }
}
