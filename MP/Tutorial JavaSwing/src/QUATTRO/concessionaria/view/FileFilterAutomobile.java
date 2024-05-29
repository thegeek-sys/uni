package QUATTRO.concessionaria.view;

import javax.swing.filechooser.FileFilter;
import java.io.File;

public class FileFilterAutomobile extends FileFilter {

    @Override
    public boolean accept(File f) {
        if (f.isDirectory()) return true;
        String fName = f.getName();
        int i = fName.lastIndexOf(".");
        String ext = i>0 && i<fName.length()-1 ? fName.substring(i+1).toLowerCase() : "";
        return ext.equals("car");
    }

    @Override
    public String getDescription() {
        return "File Automobile (*.car)";
    }
}
