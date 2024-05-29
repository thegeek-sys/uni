package QUATTRO.concessionaria.view;

import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Calendar;

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

    private JLabel labelBagagliaio;
    private JList listaBagagliaio;

    private JLabel labelAlimentazione;
    private JComboBox comboAlimentazione;

    private JLabel labelImmatricolazione;
    private JSpinner spinnerImmatricolazione;

    private JLabel labelCilindrata;
    private JSlider sliderCilindrata;

    private JLabel labelColore;
    private JButton buttonColore;

    private FormListener formListener;

    PannelloForm() {
        // imposto le dimensioni della sidebar
        Dimension dimensioni = getPreferredSize();
        dimensioni.width = 340;
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

        // Bagagliaio
        labelBagagliaio = new JLabel("Bagaiaio: ");
        listaBagagliaio = new JList();
        listaBagagliaio.setPreferredSize(new Dimension(185, 55));
        listaBagagliaio.setBorder(BorderFactory.createEtchedBorder());
        DefaultListModel modelloBagaliaio = new DefaultListModel();
        // non rispetta modello MVC (modello non è separato)
        // modelloBagaliaio.addElement("Piccolo");
        // modelloBagaliaio.addElement("Medio");
        // modelloBagaliaio.addElement("Grande");
        modelloBagaliaio.addElement(new Bagagliaio(0, "Piccolo"));
        modelloBagaliaio.addElement(new Bagagliaio(1, "Medio"));
        modelloBagaliaio.addElement(new Bagagliaio(2, "Grande"));

        listaBagagliaio.setModel(modelloBagaliaio);
        listaBagagliaio.setSelectedIndex(0);

        // Alimentazione
        labelAlimentazione = new JLabel("Alimentazione: ");
        String[] opzioniAlimentazione = {"Benzina", "Disel", "GPL", "Elettrico", "Metano"};
        comboAlimentazione = new JComboBox(opzioniAlimentazione);
        comboAlimentazione.setSelectedIndex(0);
        // visto che sto rendendo possibile all'utente di aggiungere una nuova opzione non presente nel menu
        // non posso più fare in modo di separare model e view come invece avevo fatto per bagagliaio
        comboAlimentazione.setEditable(true);

        // Immatricolazione
        labelImmatricolazione = new JLabel("Immatricolazione: ");
        spinnerImmatricolazione = new JSpinner();
        int currentYear = Calendar.getInstance().get(Calendar.YEAR);
        SpinnerNumberModel modelloImmatricolazione = new SpinnerNumberModel(currentYear, currentYear-100, currentYear, 1);
        spinnerImmatricolazione.setModel(modelloImmatricolazione);
        JSpinner.NumberEditor editor = new JSpinner.NumberEditor(spinnerImmatricolazione, "#");
        spinnerImmatricolazione.setEditor(editor);

        // Cilindrata
        labelCilindrata = new JLabel("Cilindrata: ");
        sliderCilindrata = new JSlider(900, 2000);
        sliderCilindrata.setMajorTickSpacing(300);
        sliderCilindrata.setMinorTickSpacing(50);
        sliderCilindrata.setPaintTicks(true);
        sliderCilindrata.setPaintLabels(true);
        sliderCilindrata.setSnapToTicks(true);

        // Colore
        labelColore = new JLabel("Colore auto: ");
        buttonColore = new JButton("Seleziona colore");
        buttonColore.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Color colore = JColorChooser.showDialog(new JFrame(), "Seleziona un colore", Color.RED);
                buttonColore.setBackground(colore);
                // buttonColore.setOpaque(true);
            }
        });

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
                int bagagliaio = ((Bagagliaio)listaBagagliaio.getSelectedValue()).getId();
                String alimentazione = (String)comboAlimentazione.getSelectedItem();
                int immatricolazione = (int)spinnerImmatricolazione.getValue();
                int cilindrata  = sliderCilindrata.getValue();
                int colore = buttonColore.getBackground().getRGB();
                String coloreHex = Integer.toHexString(colore);

                FormEvent formEvent = new FormEvent(this, marca, modello, vendita, targa, cambio, bagagliaio, alimentazione, immatricolazione, cilindrata, coloreHex);

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

        // RIGA 5: label Bagagliaio
        gbc.gridx = 0;
        gbc.gridy = 4;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.FIRST_LINE_END;
        gbc.insets = new Insets(0,0,0,5);
        add(labelBagagliaio, gbc);

        // RIGA 5: list Bagagliaio
        gbc.gridx = 1;
        gbc.gridy = 4;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_START;
        gbc.insets = new Insets(0,0,0,0);
        add(listaBagagliaio, gbc);

        // RIGA 6: label Alimentazione
        gbc.gridx = 0;
        gbc.gridy = 5;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_END;
        gbc.insets = new Insets(0,0,0,5);
        add(labelAlimentazione, gbc);

        // RIGA 6: combo Alimentazione
        gbc.gridx = 1;
        gbc.gridy = 5;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_START;
        gbc.insets = new Insets(5,0,0,0);
        add(comboAlimentazione, gbc);

        // RIGA 7: label Immatricolazione
        gbc.gridx = 0;
        gbc.gridy = 6;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_END;
        gbc.insets = new Insets(0,0,0,5);
        add(labelImmatricolazione, gbc);

        // RIGA 7: spinner Immatricolazione
        gbc.gridx = 1;
        gbc.gridy = 6;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_START;
        gbc.insets = new Insets(0,0,0,0);
        add(spinnerImmatricolazione, gbc);

        // RIGA 8: label Cilindrata
        gbc.gridx = 0;
        gbc.gridy = 7;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_END;
        gbc.insets = new Insets(0,0,0,5);
        add(labelCilindrata, gbc);

        // RIGA 8: slider Cilindrata
        gbc.gridx = 1;
        gbc.gridy = 7;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_START;
        gbc.insets = new Insets(0,0,0,0);
        add(sliderCilindrata, gbc);

        // RIGA 9: label Vendita
        gbc.gridx = 0;
        gbc.gridy = 8;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_END;
        gbc.insets = new Insets(0,0,0,5);
        add(labelColore, gbc);

        // RIGA 9: checkBox Vendita
        gbc.gridx = 1;
        gbc.gridy = 8;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_START;
        gbc.insets = new Insets(0,0,0,0);
        add(buttonColore, gbc);

        // RIGA 10: label Vendita
        gbc.gridx = 0;
        gbc.gridy = 9;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_END;
        gbc.insets = new Insets(0,0,0,5);
        add(labelVendita, gbc);

        // RIGA 10: checkBox Vendita
        gbc.gridx = 1;
        gbc.gridy = 9;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_START;
        gbc.insets = new Insets(0,0,0,0);
        add(checkVendita, gbc);

        // RIGA 11: label Modello
        gbc.gridx = 0;
        gbc.gridy = 10;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_END;
        gbc.insets = new Insets(0,0,0,5);
        add(labelTarga, gbc);

        // RIGA 11: field Modello
        gbc.gridx = 1;
        gbc.gridy = 10;
        gbc.weightx = 0.01;
        gbc.weighty = 0.01;
        gbc.anchor = GridBagConstraints.LINE_START;
        gbc.insets = new Insets(0,0,0,0);
        add(fieldTarga, gbc);

        // RIGA 12: Bottone
        gbc.gridx = 0;
        gbc.gridy = 11;
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

class Bagagliaio {
    private int id;
    private String nome;

    public Bagagliaio(int id, String nome) {
        this.id = id;
        this.nome = nome;
    }

    public int getId() {
        return id;
    }

    @Override
    public String toString() {
        return nome;
    }
}