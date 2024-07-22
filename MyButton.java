import java.awt.*;
import javax.swing.*;

public class MyButton extends JButton {
    private int row;
    private int column;
    private int number;


    public MyButton(int row, int column, int number) {
        super(String.valueOf(number));
        this.row = row;
        this.column = column;
        this.number = number;

        setFont(new Font("Arial", Font.BOLD, 60));
        this.setBackground(new Color(0xfadbc8));
    }


    public int getRow() {
        return row;
    }

    public void setRow(int row) {
        this.row = row;
    }

    public int getColumn() {
        return column;
    }

    public void setColumn(int column) {
        this.column = column;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
}

