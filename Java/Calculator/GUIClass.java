import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.awt.event.ActionEvent;
import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JTextField;
import javax.swing.JCheckBox;
import javax.swing.JOptionPane;

public class GUIClass extends JFrame {
	private static final long serialVersionUID = 1L;
	private JTextField tfInput;
	private JButton bSquareBy2;
	private JButton bSquareRootBy2;
	private JButton bSquare;
	private JButton bSquareRoot;
	private JCheckBox cbBold;
	private JCheckBox cbItalic;
	
	public GUIClass () {
		super ("Calculator");
		setLayout (new FlowLayout ());
		ActionactionHandlerClass actionHandler = new ActionactionHandlerClass ();
		ItemHandlerClass itemHandler = new ItemHandlerClass ();
		
		tfInput = new JTextField ("", 20);
		tfInput.setToolTipText ("Enter the numbers here");
		tfInput.setFont (new Font ("Times New Roman", Font.PLAIN, 14));
		add (tfInput);
		
		bSquareBy2 = new JButton ("x*2");
		bSquareBy2.setToolTipText ("Multiply by 2");
		bSquareBy2.addActionListener (actionHandler);
		add (bSquareBy2);
		
		bSquareRootBy2 = new JButton ("x/2");
		bSquareRootBy2.setToolTipText ("Divide by 2");
		bSquareRootBy2.addActionListener (actionHandler);
		add (bSquareRootBy2);
		
		bSquare = new JButton ("x²");
		bSquare.setToolTipText ("Square");
		bSquare.addActionListener (actionHandler);
		add (bSquare);
		
		bSquareRoot = new JButton ("√x");
		bSquareRoot.setToolTipText ("Square root");
		bSquareRoot.addActionListener (actionHandler);
		add (bSquareRoot);
		
		cbBold = new JCheckBox ("Bold", false);
		cbBold.setToolTipText ("Bold");
		cbBold.addItemListener (itemHandler);
		add (cbBold);
		
		cbItalic = new JCheckBox ("Italic", false);
		cbItalic.setToolTipText ("Italic");
		cbItalic.addItemListener (itemHandler);
		add (cbItalic);
	}
	
	public class ActionactionHandlerClass implements ActionListener {
		public void actionPerformed (ActionEvent ae) {
			if (ae.getSource () == bSquareBy2) {
				tfInput.setText (Long.toString (Long.parseLong (tfInput.getText ()) * 2));
			}
			if (ae.getSource () == bSquareRootBy2) {
				tfInput.setText (Long.toString (Long.parseLong (tfInput.getText ()) / 2));
			}
			if (ae.getSource () == bSquare) {
				tfInput.setText (Long.toString (Long.parseLong (tfInput.getText ()) * Long.parseLong(tfInput.getText ())));
			}
			if (ae.getSource () == bSquareRoot) {
				tfInput.setText (Double.toString (Math.sqrt (Long.parseLong (tfInput.getText ()))));
			}
		}
	}
	
	public class ItemHandlerClass implements ItemListener {
		public void itemStateChanged (ItemEvent ie) {
			Font font = null;
			if (cbBold.isSelected () && cbItalic.isSelected ()) {
				font = new Font ("Times New Roman", Font.ITALIC + Font.BOLD, 14);
			}
			else if (cbBold.isSelected ()) {
				font = new Font ("Times New Roman", Font.BOLD, 14);
			}
			else if (cbItalic.isSelected ()) {
				font = new Font ("Times New Roman", Font.ITALIC, 14);
			}
			else {
				font = new Font ("Times New Roman", Font.PLAIN, 14);
			}
			tfInput.setFont (font);
		}
	}
}