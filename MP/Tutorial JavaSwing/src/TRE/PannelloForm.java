package TRE;

import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;

public class PannelloForm extends JPanel {
    PannelloForm() {
        // imposto le dimensioni della sidebar
        Dimension dimensioni = getPreferredSize();
        dimensioni.width = 300;
        setPreferredSize(dimensioni);
        // oppure
        // setPreferredSize(new Dimension(300,100));

        Border bordoInterno = BorderFactory.createTitledBorder("Aggiungi Automobile");
        Border bordoEsterno = BorderFactory.createEmptyBorder(0,5,5,5);
        Border bordoFinale = BorderFactory.createCompoundBorder(bordoEsterno, bordoInterno);
        setBorder(bordoFinale);
    }
}
