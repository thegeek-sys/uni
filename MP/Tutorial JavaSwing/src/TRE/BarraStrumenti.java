package TRE;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class BarraStrumenti extends JPanel implements ActionListener {

    private JButton bottoneBuongiorno;
    private JButton bottoneBuonasera;
    private JButton cliccamiTiPrego;
    private TextAreaPanel textAreaPanel;

    public BarraStrumenti() {

        cliccamiTiPrego = new JButton("Cliccami ti prego");
        bottoneBuongiorno = new JButton("Buongiorno!");
        bottoneBuonasera = new JButton("Buonasera!");

        bottoneBuongiorno.addActionListener(this);
        bottoneBuonasera.addActionListener(this);
        cliccamiTiPrego.addActionListener(this);

        setLayout(new FlowLayout(FlowLayout.LEFT, 5, 5));

        add(bottoneBuongiorno);
        add(bottoneBuonasera);
        add(cliccamiTiPrego);

    }

    public void setTextAreaPanel(TextAreaPanel textAreaPanel) {
        this.textAreaPanel = textAreaPanel;
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        JButton premuto = (JButton)e.getSource();

        if (premuto == bottoneBuongiorno) {
            textAreaPanel.appendiTesto("Buongiorno !!!");
        } else if (premuto == bottoneBuonasera) {
            textAreaPanel.appendiTesto("Buonasera !!!");
        }
    }
}
