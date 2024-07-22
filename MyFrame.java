import java.awt.BorderLayout;
import java.awt.Color;

import javax.swing.*;

class MyFrame extends JFrame {
    private MyPanel panel;
    private MyMenu menuBar;

    public MyFrame() {
        panel = new MyPanel();
        menuBar = new MyMenu(panel);

        setTitle("Пятнашки");
        setSize(500, 500);
        setLayout(new BorderLayout());
        setResizable(false);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        ImageIcon image = new ImageIcon("лого игры.png");
        setIconImage(image.getImage());
        getContentPane().setBackground(new Color(0xFBCEB1));
        panel.setOpaque(false);

        setJMenuBar(menuBar);
        add(panel);

        setVisible(true);
    }
}
