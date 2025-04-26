import java.util.Scanner;   
public class Exp1a
{
   public static void factorial(int num)
   {
     int fact=1;
     for(int i=1;i<=num;i++)
     {
       fact=fact*i;
     }
    System.out.println("factorial is:"+fact);
   }
 
  public static void reverse(int n1)
  {
    int sum=0 , remain;
    while(n1!=0)
    {
    remain=n1%10;
    sum=sum*10+remain;
    n1/=10;
    }
    System.out.println("reverse of the number is:"+n1);
  }

  public static void main(String[] args)
  {
    Scanner sc=new Scanner(System.in);
    int num=0;
    System.out.println("Enter your choice: 1.factorial 2.Reverse");
    int choice=sc.nextInt();
    while(1)
   {
    switch(choice)
    {
     case 1:
       System.out.println("Enter a value to find factorial:");
       num=sc.nextInt();
       factorial(num);
       break;
     case 2:
       System.out.println("Enter the number to be reversed:");
       num=sc.nextInt();
       reverse(num);
       break;
    }
  } }
}