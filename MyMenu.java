
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.*;

import javax.swing.*;

class MyMenu extends JMenuBar {

    public MyMenu(MyPanel game) {

        JMenuBar menuBar = new JMenuBar();
        //элементы меню и мнемоники
        JMenu file = new JMenu("File");
        JMenu help = new JMenu("Help");
        file.setMnemonic(KeyEvent.VK_F);
        help.setMnemonic(KeyEvent.VK_H);
        //подпункт меню - NEW
        JMenuItem fileNew = new JMenuItem("New");
        fileNew.setMnemonic(KeyEvent.VK_N);
        fileNew.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_N, ActionEvent.ALT_MASK));
        fileNew.addActionListener(new ActionListener() { //обработка события (что происходит при нажатии)
            @Override
            public void actionPerformed(ActionEvent e) {
                game.generateField();
            }
        });
        //подпункт меню - EXIT
        JMenuItem fileExit = new JMenuItem("Exit");
        fileExit.setMnemonic(KeyEvent.VK_E);
        fileExit.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_E, ActionEvent.ALT_MASK));
        fileExit.addActionListener(new ActionListener() { //обработка события (что происходит при нажатии)
            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });
        //подпункт меню - ABOUT
        JMenuItem helpAbout = new JMenuItem("About");
        helpAbout.setMnemonic(KeyEvent.VK_A);
        helpAbout.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_3, ActionEvent.ALT_MASK));
        helpAbout.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) { //при нажатии открывается диалоговое окно
                JDialog dialog = new JDialog();
                dialog.setSize(300, 200);
                dialog.setResizable(false);
                dialog.setLocationRelativeTo(null); //выравниваем по центру
                ImageIcon about_logo = new ImageIcon("about_logo.png"); //создали иконку диалогового окна
                dialog.setIconImage(about_logo.getImage()); //установили эту иконку
                // чтобы объекты в диалоговом окне отображались в нужном порядке, используем менеджер компоновки
                dialog.setLayout(new BorderLayout());
                JPanel panel = new JPanel(); // эта панель будет в диалоговом окне, и она будет содержать labels с именем,группой,годом и кнопку
                dialog.getContentPane().setBackground(new Color(0xffe4e1));
                panel.setOpaque(false);
                panel.setLayout(new GridLayout(0,1)); //делаем так чтобы в колоночку наши label расположились
                panel.add(createLabel("Автор: Базилевич Мария"));
                panel.add(createLabel("Группа: P3166"));
                panel.add(createLabel("Год: 2023"));

                JButton button = new JButton("А она хороша!");
                button.setBackground(new Color(0xffcbbb));
                button.addActionListener(new ActionListener() {  //обработка событий щелчок мыши
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        dialog.dispose(); //при нажатии на кнопку диалоговое окно закроется
                    }
                });
                button.addKeyListener(new KeyListener() { //обработка событий клавиатуры
                    @Override
                    public void keyTyped(KeyEvent e) {
                    }
                    @Override
                    public void keyPressed(KeyEvent e) {
                        if(e.getKeyCode() == KeyEvent.VK_ENTER){ //если нажмём enter или space, диалоговое окно закроется
                            dialog.dispose();
                        }
                    }
                    @Override
                    public void keyReleased(KeyEvent e) {
                    }
                });

                panel.add(button);
                dialog.add(panel);
                dialog.setVisible(true);
            }
        });
        JMenuItem check_win = new JMenuItem("Win");
        check_win.setMnemonic(KeyEvent.VK_W);
        check_win.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_W, InputEvent.CTRL_DOWN_MASK));
        check_win.addActionListener(e -> game.test_win());

        //добавляем эти пункты и подпункты
        file.add(fileNew);
        file.add(fileExit);
        help.add(helpAbout);
        help.add(check_win);
        menuBar.add(file);
        menuBar.add(help);
        add(menuBar, BorderLayout.NORTH);
    }

    //метод создаёт unselectable text, настраивая выравнивание по левому краю и определив нужный шрифт
    private JLabel createLabel(String text) {
        JLabel label = new JLabel(text);
        label.setHorizontalAlignment(SwingConstants.LEFT);
        label.setFont(new Font("Arial", Font.TRUETYPE_FONT, 20));
        return label;
    }
}