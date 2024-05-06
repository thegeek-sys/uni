package TRE;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Frame extends JFrame {

    private TextAreaPanel textAreaPanel;private BarraStrumenti barraStrumenti;
    private PannelloForm pannelloForm;

    public Frame() {
        super("Finestra numero 1");

        setLayout(new BorderLayout());

        barraStrumenti = new BarraStrumenti();
        textAreaPanel = new TextAreaPanel();
        pannelloForm = new PannelloForm();

        barraStrumenti.setTextAreaPanel(textAreaPanel);

        pannelloForm.setFormListener(new FormListener() {
            @Override
            public void formEventListener(FormEvent fe) {
                String marca = fe.getMarca();
                String modello = fe.getModello();
                boolean vendita = fe.isVendita();
                String targa = fe.getTarga();
                String cambio = fe.getCambio();

                textAreaPanel.appendiTesto("Marca: "+marca);
                textAreaPanel.appendiTesto("Modello: "+modello);
                textAreaPanel.appendiTesto("Venduta: "+vendita);
                textAreaPanel.appendiTesto("Targa: "+targa);
                textAreaPanel.appendiTesto("Cambio: "+cambio);
                textAreaPanel.appendiTesto("");

            }
        });

        add(barraStrumenti, BorderLayout.PAGE_START);
        add(textAreaPanel, BorderLayout.CENTER);
        add(pannelloForm, BorderLayout.LINE_START);

        setSize(800,500);
        //setLocation(200,200);
        setLocationRelativeTo(null);

        //setResizable(false);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setVisible(true);
    }
}
