import java.util.Scanner;

class Area
{
 double len, bre;
 void setDim(double len,double bre)
{
  this.len=len;
  this.bre=bre;
}
 void getArea()
{
  System.out.println("area of rectangle\t"+(len*bre));
}
}
 
public class Exp3b{
  public static void main(String[] args)
  {
   double l1,b1;
   Scanner sc=new Scanner(System.in);
   System.out.println("enter the values of length and breadth");
   l1=sc.nextDouble();
   b1=sc.nextDouble();
   Area a1=new Area();
   a1.setDim(l1,b1);
   a1.getArea();
 }
}
    