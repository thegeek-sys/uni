package TRE;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.InputEvent;
import java.awt.event.KeyEvent;

public class Frame extends JFrame {

    private TextAreaPanel textAreaPanel;
    private BarraStrumenti barraStrumenti;
    private PannelloForm pannelloForm;
    private JFileChooser fileChooser;

    public Frame() {
        super("Finestra numero 1");

        setLayout(new BorderLayout());

        setJMenuBar(creaBarraMenu());

        barraStrumenti = new BarraStrumenti();
        textAreaPanel = new TextAreaPanel();
        pannelloForm = new PannelloForm();

        fileChooser = new JFileChooser();
        fileChooser.addChoosableFileFilter(new FileFilterAutomobile());
        fileChooser.setAcceptAllFileFilterUsed(false);

        barraStrumenti.setTextAreaPanel(textAreaPanel);

        pannelloForm.setFormListener(new FormListener() {
            @Override
            public void formEventListener(FormEvent fe) {
                String marca = fe.getMarca();
                String modello = fe.getModello();
                boolean vendita = fe.isVendita();
                String targa = fe.getTarga();
                String cambio = fe.getCambio();
                String alimentazione = fe.getAlimentazione();
                int immatricolazione = fe.getImmatricolazione();
                int cilindrata = fe.getCilindrata();
                String colore = fe.getColore();

                String bagagliaio = switch (fe.getBagagliaio()) {
                    case 0 -> "piccolo";
                    case 1 -> "medio";
                    case 2 -> "grande";
                    default -> throw new IllegalStateException("Unexpected value: " + fe.getBagagliaio());
                };

                textAreaPanel.appendiTesto("Marca: "+marca);
                textAreaPanel.appendiTesto("Modello: "+modello);
                textAreaPanel.appendiTesto("Venduta: "+vendita);
                textAreaPanel.appendiTesto("Targa: "+targa);
                textAreaPanel.appendiTesto("Cambio: "+cambio);
                textAreaPanel.appendiTesto("Bagagliaio: "+bagagliaio);
                textAreaPanel.appendiTesto("Alimentazione: "+alimentazione);
                textAreaPanel.appendiTesto("Immatricolazione: "+immatricolazione);
                textAreaPanel.appendiTesto("Cilindrata: "+cilindrata);
                textAreaPanel.appendiTesto("Colore: "+colore);
                textAreaPanel.appendiTesto("");

            }
        });

        add(barraStrumenti, BorderLayout.PAGE_START);
        add(textAreaPanel, BorderLayout.CENTER);
        add(pannelloForm, BorderLayout.LINE_START);

        //setSize(800,550);
        setMinimumSize(new Dimension(800, 530));
        //setLocation(200,200);
        setLocationRelativeTo(null);

        //setResizable(false);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setVisible(true);
    }

    private JMenuBar creaBarraMenu() {
        JMenuBar barraMenu = new JMenuBar();

        JMenu menuFile = new JMenu("File");
        menuFile.setMnemonic(KeyEvent.VK_F); // non worka su macos

        JMenuItem menuItemOpen = new JMenuItem("Open...", new ImageIcon("./src/import.png"));
        JMenuItem menuItemExport = new JMenuItem("Export...", new ImageIcon("./src/export.png"));
        JMenuItem menuItemQuit = new JMenuItem("Quit");
        menuItemQuit.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_X, InputEvent.META_DOWN_MASK));

        menuFile.add(menuItemOpen);
        menuFile.add(menuItemExport);
        menuFile.addSeparator();
        menuFile.add(menuItemQuit);

        JMenu menuFinestra = new JMenu("Window");
        JMenu menuMostra = new JMenu("Mostra");
        JCheckBoxMenuItem menuItemMostraForm = new JCheckBoxMenuItem("Mostra form");
        menuItemMostraForm.setSelected(true);

        menuItemMostraForm.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JCheckBoxMenuItem menuItem = (JCheckBoxMenuItem)e.getSource();
                pannelloForm.setVisible(menuItem.isSelected());
            }
        });

        menuItemQuit.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int azioneFinestra = JOptionPane.showConfirmDialog(Frame.this, "Vuoi uscire?", "Chiusura applicazione", JOptionPane.OK_CANCEL_OPTION, JOptionPane.QUESTION_MESSAGE);
                if (azioneFinestra == JOptionPane.OK_OPTION) {
                    System.exit(0);
                }
            }
        });

        menuItemOpen.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (fileChooser.showOpenDialog(Frame.this) == JFileChooser.APPROVE_OPTION) {
                    System.out.println(fileChooser.getSelectedFile());
                }
            }
        });

        menuItemExport.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (fileChooser.showSaveDialog(Frame.this) == JFileChooser.APPROVE_OPTION) {
                    System.out.println(fileChooser.getSelectedFile());
                }
            }
        });

        menuMostra.add(menuItemMostraForm);
        menuFinestra.add(menuMostra);

        barraMenu.add(menuFile);
        barraMenu.add(menuFinestra);

        return  barraMenu;
    }
}
