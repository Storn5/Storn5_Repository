
public class MainClass
{
	public static void main(String[] args)
	{
		double a;
        double b;
        double c;
        double D;
        double x1;
        double x2;
        
        System.out.println("Insert value of the 1st number");
        a=Double.parseDouble(System.console().readLine());
        System.out.println("Insert value of the 2nd number");  
        b=Double.parseDouble(System.console().readLine());
        System.out.println("Insert value of the 3rd number");
        c=Double.parseDouble(System.console().readLine());
        
        D=(Math.pow(b,2))-4*a*c;
        
        if (D>0)
        {
            x1=(-b-(Math.sqrt(D)))/2*a;
            x2=(-b+(Math.sqrt(D)))/2*a;
            System.out.println(x1);
            System.out.println(x2);
        }
        else if (D==0)
        {
                x1=(-b-0)/2*a;
                System.out.println(x1);
        }
        else
        {
        	System.out.println("/0/");
        }
	}
}