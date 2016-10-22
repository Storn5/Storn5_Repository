import java.util.Scanner;

public class MainClass
{
	static Scanner input = new Scanner(System.in);
	public static void main(String[] args)
	{
		char func;
		double a, b;
		String tempStr;
		System.out.print("Choose a function (+, -, *, /): ");
		func = input.next().charAt(0);
		System.out.print("Enter the first number: ");
		tempStr = input.next();
		a = Double.parseDouble(tempStr);
		System.out.print("Enter the second number: ");
		tempStr = input.next();
		b = Double.parseDouble(tempStr);
		switch(func)
		{
		case '+':
			Add(a, b);
			break;
		case '-':
			Subtract(a, b);
			break;
		case '*':
			Multiply(a, b);
			break;
		case '/':
			Divide(a, b);
			break;
		default:
			Error();
			break;
		}
	}
	static void Add(double x, double y)
	{
		System.out.println(x+y);
	}
	static void Subtract(double x, double y)
	{
		System.out.println(x-y);
	}
	static void Multiply(double x, double y)
	{
		System.out.println(x*y);
	}
	static void Divide(double x, double y)
	{
		System.out.println(x/y);
	}
	static void Error()
	{
		System.out.println("You entered a non-existing function.");
	}
}