package UNO;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Frame extends JFrame {

    private JTextArea textArea;   // textArea
    private JTextField textField; // textField
    private JButton button;

    public Frame() {
        super("Finestra numero 1");

        setLayout(new BorderLayout());

        textArea = new JTextArea();
        textField = new JTextField();
        button = new JButton("Cliccami ti prego");

        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // textArea.append("DIOCANEE\n");
                String testoTextField = textField.getText();
                if (!testoTextField.equals("")) {
                    textArea.append(testoTextField+"\n");
                    textField.setText("");
                }
            }
        });

        add(textArea, BorderLayout.CENTER);
        add(button, BorderLayout.PAGE_END);
        add(textField, BorderLayout.PAGE_START);


        setSize(800,500);
        //setLocation(200,200);
        setLocationRelativeTo(null);

        //setResizable(false);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setVisible(true);
    }
}
