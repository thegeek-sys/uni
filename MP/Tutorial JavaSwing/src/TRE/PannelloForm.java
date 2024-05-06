package TRE;

import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class PannelloForm extends JPanel {

    private JLabel labelMarca;
    private JLabel labelModello;

    private JTextField fieldMarca;
    private JTextField fieldModello;

    private JButton bottoneAggiungi;

    private JLabel labelVendita;
    private JCheckBox checkVendita;

    private JLabel labelTarga;
    private JTextField fieldTarga;

    private JLabel labelCambio;
    private JRadioButton radioCambioManuale;
    private JRadioButton radioCambioAutomatico;
    private ButtonGroup gruppoRadioCambio;

    private FormListener formListener;

    PannelloForm() {
        // imposto le dimensioni della sidebar
        Dimension dimensioni = getPreferredSize();
        dimensioni.width = 330;
        setPreferredSize(dimensioni);
        // oppure
        // setPreferredSize(new Dimension(300,100));

        setLayout(new GridBagLayout());

        Border bordoInterno = BorderFactory.createTitledBorder("Aggiungi Automobile");
        Border bordoEsterno = BorderFactory.createEmptyBorder(0,5,5,5);
        Border bordoFinale = BorderFactory.createCompoundBorder(bordoEsterno, bordoInterno);
        setBorder(bordoFinale);

        // Marca
        labelMarca = new JLabel("Marca: ");
        fieldMarca = new JTextField(15);  // consigliato sempre aggiungere il valore
        //fieldMarca.setMinimumSize(new Dimension(120,16));

        // Modello
        labelModello = new JLabel("Modello: ");
        fieldModello = new JTextField(15);

        // Vendita e Targa
        labelVendita = new JLabel("Vendita: ");
        checkVendita = new JCheckBox();

        labelTarga = new JLabel("Targa: ");
        fieldTarga = new JTextField(15);
        labelTarga.setEnabled(false);
        fieldTarga.setEnabled(false);

        // Cambio
        labelCambio = new JLabel("Cambio: ");
        radioCambioManuale = new JRadioButton("Manuèl");
        radioCambioManuale.setActionCommand("manuale");
        radioCambioManuale.setSelected(true);

        radioCambioAutomatico = new JRadioButton("Automatico");
        radioCambioAutomatico.setActionCommand("automatico");

        gruppoRadioCambio = new ButtonGroup();
        gruppoRadioCambio.add(radioCambioManuale);
        gruppoRadioCambio.add(radioCambioAutomatico);


        checkVendita.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                boolean selezione = checkVendita.isSelected();

                labelTarga.setEnabled(selezione);
                fieldTarga.setEnabled(selezione);

                if (!selezione) fieldTarga.setText("");
            }
        });

        // Bottone
        bottoneAggiungi = new JButton("Aggiungi!");
        bottoneAggiungi.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String marca = fieldMarca.getText();
                String modello = fieldModello.getText();
                boolean vendita = checkVendita.isSelected();
                String targa = fieldTarga.getText();
                String cambio = gruppoRadioCambio.getSelection().getActionCommand();

                FormEvent formEvent = new FormEvent(this, marca, modello, vendita, targa, cambio);

                if (formListener != null) {
                    formListener.formEventListener(formEvent);
                }
            }
        });

        // layout
        GridBagConstraints gbc = new GridBagConstraints();

        // RIGA 1: label Marca
        // definire posizione x e y dell'inizio della cella
        gbc.gridx = 0;
        gbc.gridy = 0;

        // il peso controlla quanto spazio una cella occupa rispetto a un'altra cella
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;

        gbc.anchor = GridBagConstraints.LINE_END;

        gbc.insets = new Insets(0,0,0,5); // aggiungo del bordo a destra

        add(labelMarca, gbc);

        // RIGA 1: field Marca
        // la doc di java ci consiglia di creare un nuovo oggetto per ogni componente
        // ma qui preferiamo direttamente sovrascrivere i valori precedentemente assegnati
        gbc.gridx = 1;
        gbc.gridy = 0;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_START;
        gbc.insets = new Insets(0,0,0,0);
        add(fieldMarca, gbc);

        // RIGA 2: label Modello
        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_END;
        gbc.insets = new Insets(0,0,0,5);
        add(labelModello, gbc);

        // RIGA 2: field Modello
        gbc.gridx = 1;
        gbc.gridy = 1;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_START;
        gbc.insets = new Insets(0,0,0,0);
        add(fieldModello, gbc);

        // RIGA 3: label Cambio
        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_END;
        gbc.insets = new Insets(0,0,0,5);
        add(labelCambio, gbc);

        // RIGA 3: radio CambioManuale
        gbc.gridx = 1;
        gbc.gridy = 2;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_START;
        gbc.insets = new Insets(0,0,0,0);
        add(radioCambioManuale, gbc);

        // RIGA 4: radio CambioAutomatico
        gbc.gridx = 1;
        gbc.gridy = 3;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_START;
        gbc.insets = new Insets(0,0,0,0);
        add(radioCambioAutomatico, gbc);

        // RIGA 5: label Vendita
        gbc.gridx = 0;
        gbc.gridy = 4;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_END;
        gbc.insets = new Insets(0,0,0,5);
        add(labelVendita, gbc);

        // RIGA 5: field Vendita
        gbc.gridx = 1;
        gbc.gridy = 4;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_START;
        gbc.insets = new Insets(0,0,0,0);
        add(checkVendita, gbc);

        // RIGA 6: label Modello
        gbc.gridx = 0;
        gbc.gridy = 5;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_END;
        gbc.insets = new Insets(0,0,0,5);
        add(labelTarga, gbc);

        // RIGA 6: field Modello
        gbc.gridx = 1;
        gbc.gridy = 5;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_START;
        gbc.insets = new Insets(0,0,0,0);
        add(fieldTarga, gbc);

        // RIGA 7: Bottone
        gbc.gridx = 0;
        gbc.gridy = 6;
        gbc.weightx = 1.0;
        gbc.weighty = 1.0;
        gbc.gridwidth = 2;
        gbc.gridheight = 1;
        gbc.anchor = GridBagConstraints.PAGE_START;
        gbc.insets = new Insets(0,0,0,0);

        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.ipady = 15;

        add(bottoneAggiungi, gbc);
    }

    public void setFormListener(FormListener formListener) {
        this.formListener = formListener;
    }
}
