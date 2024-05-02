package TRE;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Frame extends JFrame {

    private TextAreaPanel textAreaPanel;
    private JButton button;
    private BarraStrumenti barraStrumenti;
    private PannelloForm pannelloForm;

    public Frame() {
        super("Finestra numero 1");

        setLayout(new BorderLayout());

        barraStrumenti = new BarraStrumenti();
        textAreaPanel = new TextAreaPanel();
        button = new JButton("Cliccami ti prego");
        pannelloForm = new PannelloForm();

        barraStrumenti.setTextAreaPanel(textAreaPanel);

        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // textArea.append("DIOCANEE\n");
                textAreaPanel.appendiTesto("Ciao"+"\n");
            }
        });

        add(barraStrumenti, BorderLayout.PAGE_START);
        add(textAreaPanel, BorderLayout.CENTER);
        add(button, BorderLayout.PAGE_END);
        add(pannelloForm, BorderLayout.LINE_START);

        setSize(800,500);
        //setLocation(200,200);
        setLocationRelativeTo(null);

        //setResizable(false);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setVisible(true);
    }
}
