package QUATTRO.concessionaria.view;

import javax.swing.*;
import java.awt.*;

public class TextAreaPanel extends JPanel {
    private JTextArea textArea;

    public TextAreaPanel() {
        textArea = new JTextArea();

        setLayout(new BorderLayout());

        add(new JScrollPane(textArea), BorderLayout.CENTER);
    }

    public void appendiTesto(String testo) {
        textArea.append(testo+"\n");
    }
}
