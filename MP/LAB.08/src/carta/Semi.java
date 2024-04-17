package carta;

public enum Semi {
    CUORI("cuori"), QUADRI("quadri"), FIORI("fiori"), PICCHE("picche");
    private final String seme;
    Semi(String seme) {
        this.seme = seme;
    }

    public String getSeme() { return seme; }
}
