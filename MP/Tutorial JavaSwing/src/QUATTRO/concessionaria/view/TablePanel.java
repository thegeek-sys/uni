package QUATTRO.concessionaria.view;

import QUATTRO.concessionaria.model.Auto;

import javax.swing.*;
import java.awt.*;
import java.util.List;

public class TablePanel extends JPanel {
    private JTable table;
    private TableModelAuto tableModelAuto;

    public TablePanel() {

        tableModelAuto = new TableModelAuto();

        table = new JTable(tableModelAuto);

        setLayout(new BorderLayout());
        add(new JScrollPane(table), BorderLayout.CENTER);

    }

    public void setData(List<Auto> listaAutomobili) {
        tableModelAuto.setData(listaAutomobili);
    }

    public void aggiorna() {
        tableModelAuto.fireTableDataChanged();
    }
}
