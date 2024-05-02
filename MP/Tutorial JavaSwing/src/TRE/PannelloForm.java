package TRE;

import javax.swing.*;
import java.awt.*;

public class PannelloForm extends JPanel {
    PannelloForm() {
        // imposto le dimensioni della sidebar
        Dimension dimensioni = getPreferredSize();
        dimensioni.width = 300;
        setPreferredSize(dimensioni);
        // oppure
        // setPreferredSize(new Dimension(300,100));
    }
}
