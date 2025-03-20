package e08_09_23.memoria;

public class AnimaleConcreta extends Animale{
    public static int esseri_viventi;
    private int z;
    private float f;
    public AnimaleConcreta(int k) {
        super(-k);
        z = (esseri_viventi++)+k;
    }

    @Override
    public String toString() {
        return super.toString()+";AnimaleConcreata:"+(z+esseri_viventi);
    }
}
