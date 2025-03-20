package memoria;

public class C extends B{
    static int instances;
    public C() {instances=super.getInstaces();}
    public int getInstaces(){
        return instances+A.instances;
    }
}

