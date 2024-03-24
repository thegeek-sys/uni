public enum SemeCarta {
    CUORI, QUADRI, FIORI, PICCHE;

    public static void main(String[] args) {
        SemeCarta[] valori = SemeCarta.values();
        for (int k = 0; k < valori.length; k++) {
            System.out.print(valori[k]+" ");
        }

        String v = "PICCHE";
        SemeCarta picche = SemeCarta.valueOf(v);
        System.out.println(picche);
    }
}
