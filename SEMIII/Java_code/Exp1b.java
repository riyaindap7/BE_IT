import java.util.Scanner;
public class Exp1b
{
  public static void main(String[] args)
  {
    int empno;
    String ename;
    double bas_sal;
    
    Scanner sc= new Scanner(System.in);
    System.out.println("enter employee name:");
      ename=sc.next();
    System.out.println("enter employee number:");
      empno=sc.nextInt();
    System.out.println("enter basic salary:");
      bas_sal=sc.nextDouble();
      
      double DA= 0.7*bas_sal;
      double HRA= 0.3*bas_sal;
      double CCA= 240;
      double PF=0.1*bas_sal;
      double PT=100;
  
    double gross_sal=bas_sal+DA+HRA+CCA;
    double net_sal=gross_sal-PF-PT;

    System.out.println("gross salary is:"+gross_sal);
    System.out.println("net salaryis:"+net_sal);
  }
}