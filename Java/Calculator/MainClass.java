import javax.swing.JFrame;

public class MainClass {
	public static void main (String args []) {
		GUIClass window = new GUIClass ();
		window.setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);
		window.setSize (250, 500);
		window.setVisible (true);
	}
}