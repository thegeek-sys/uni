package QUATTRO.concessionaria.view;

import QUATTRO.concessionaria.model.Auto;

import javax.swing.table.AbstractTableModel;
import java.util.List;

public class TableModelAuto extends AbstractTableModel {

    private List<Auto> listaAutomobili;
    private String[] nomiColonne = {"ID", "Marca", "Modello", "Vendita", "Targa", "Cambio", "Bagagliaio", "Alimentazione", "Immatricolazione", "Cilindrata", "Colore"};

    public TableModelAuto() {

    }

    public void setData(List<Auto> listaAutomobili) {
        this.listaAutomobili = listaAutomobili;
    }

    @Override
    public int getRowCount() {
        return listaAutomobili.size();
    }

    @Override
    public int getColumnCount() {
        return 11;
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        Auto auto = listaAutomobili.get(rowIndex);
        return switch (columnIndex) {
            case 0 -> auto.getId();
            case 1 -> auto.getMarca();
            case 2 -> auto.getModello();
            case 3 -> auto.isVendita();
            case 4 -> auto.getTarga();
            case 5 -> auto.getCambio().getCambio();
            case 6 -> auto.getBagagliaio().getBagagliaio();
            case 7 -> auto.getAlimentazione();
            case 8 -> auto.getImmatricolazione();
            case 9 -> auto.getCilindrata();
            case 10 -> auto.getColore();
            default -> throw new IllegalStateException("Unexpected value: " + columnIndex);
        };
    }

    @Override
    public String getColumnName(int column) {
        return nomiColonne[column];
    }
}
